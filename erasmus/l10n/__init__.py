from __future__ import annotations

from contextlib import contextmanager
from pathlib import Path
from typing import TYPE_CHECKING, Literal, TypedDict, overload

from attrs import define, field
from fluent.runtime import FluentResourceLoader

from .fluent import Localization

if TYPE_CHECKING:
    from _typeshed import SupportsItems
    from collections.abc import Iterator
    from typing_extensions import NotRequired, Unpack

    import discord
    from discord import app_commands


# These need to be mapped because pontoon uses the full code rather than the two-letter
# code that Discord uses
_fluent_locale_map = {
    'no': 'nb-NO',
    'hi': 'hi-IN',
}


def _get_fluent_locale(locale: discord.Locale) -> str:
    result = str(locale)
    if result in _fluent_locale_map:
        return _fluent_locale_map[result]
    else:
        return str(locale)


class FormatKwargs(TypedDict):
    data: NotRequired[SupportsItems[str, object] | None]


class FormatFallbackKwargs(FormatKwargs):
    use_fallbacks: bool


class FormatFallbackTrueKwargs(FormatKwargs):
    use_fallbacks: NotRequired[Literal[True]]


class FormatAnyKwargs(FormatKwargs):
    use_fallbacks: NotRequired[bool]


class LocalizerFormatKwargs(FormatKwargs):
    locale: NotRequired[discord.Locale | None]


class LocalizerFormatFallbackKwargs(LocalizerFormatKwargs, FormatFallbackKwargs):
    ...


class LocalizerFormatFallbackTrueKwargs(
    LocalizerFormatKwargs, FormatFallbackTrueKwargs
):
    ...


@define
class Localizer:
    default_locale: discord.Locale
    _loader: FluentResourceLoader = field(init=False)
    _l10n_map: dict[discord.Locale, Localization] = field(init=False)

    def __attrs_post_init__(self) -> None:
        self._loader = FluentResourceLoader(
            str(Path(__file__).resolve().parent / '{locale}')
        )
        self._l10n_map = {}

    def _create_l10n(self, locale: discord.Locale) -> Localization:
        locales = [_get_fluent_locale(locale)]

        if locale != self.default_locale:
            locales.append(_get_fluent_locale(self.default_locale))

        return Localization(locales, ['erasmus.ftl'], self._loader)

    def _get_l10n(self, locale: discord.Locale | None, /) -> Localization:
        locale = self.default_locale if locale is None else locale

        if locale in self._l10n_map:
            return self._l10n_map[locale]

        l10n = self._l10n_map[locale] = self._create_l10n(locale)

        return l10n

    @overload
    def format(
        self,
        message_id: str | app_commands.locale_str,
        /,
        **kwargs: Unpack[LocalizerFormatFallbackKwargs],
    ) -> str | None:
        ...

    @overload
    def format(
        self,
        message_id: str | app_commands.locale_str,
        /,
        **kwargs: Unpack[LocalizerFormatFallbackTrueKwargs],
    ) -> str:
        ...

    def format(
        self,
        message_id: str | app_commands.locale_str,
        /,
        *,
        locale: discord.Locale | None = None,
        data: SupportsItems[str, object] | None = None,
        use_fallbacks: bool = True,
    ) -> str | None:
        return self._get_l10n(locale).format(
            str(message_id), data, use_fallbacks=use_fallbacks
        )

    @contextmanager
    def begin_reload(self) -> Iterator[None]:
        old_map = self._l10n_map
        try:
            self._l10n_map = {}
            yield
        except Exception:
            self._l10n_map = old_map
            raise

    def for_locale(self, locale: discord.Locale, /) -> LocaleLocalizer:
        return LocaleLocalizer(self, locale)

    def for_message(
        self,
        message_id: str,
        /,
        locale: discord.Locale | None = None,
    ) -> MessageLocalizer:
        return MessageLocalizer(
            self.for_locale(self.default_locale if locale is None else locale),
            message_id,
        )


@define(frozen=True)
class LocaleLocalizer:
    localizer: Localizer
    locale: discord.Locale

    @overload
    def format(
        self,
        message_id: str | app_commands.locale_str,
        /,
        **kwargs: Unpack[FormatFallbackKwargs],
    ) -> str | None:
        ...

    @overload
    def format(
        self,
        message_id: str | app_commands.locale_str,
        /,
        **kwargs: Unpack[FormatFallbackTrueKwargs],
    ) -> str:
        ...

    def format(
        self,
        message_id: str | app_commands.locale_str,
        /,
        **kwargs: Unpack[FormatAnyKwargs],
    ) -> str | None:
        return self.localizer.format(message_id, locale=self.locale, **kwargs)


@define(frozen=True)
class MessageLocalizer:
    localizer: LocaleLocalizer
    message_id: str

    @overload
    def format(
        self,
        attribute_id: str | None = None,
        /,
        **kwargs: Unpack[FormatFallbackKwargs],
    ) -> str | None:
        ...

    @overload
    def format(
        self,
        attribute_id: str | None = None,
        /,
        **kwargs: Unpack[FormatFallbackTrueKwargs],
    ) -> str:
        ...

    def format(
        self,
        attribute_id: str | None = None,
        /,
        **kwargs: Unpack[FormatAnyKwargs],
    ) -> str | None:
        message_id = self.message_id

        if attribute_id is not None:
            message_id = f'{message_id}.{attribute_id}'

        return self.localizer.format(message_id, **kwargs)
