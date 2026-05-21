from datetime import UTC, datetime, tzinfo
from typing import Protocol, overload

from utils import cyan_print, sep_print

type Date3 = tuple[int, int, int]
type Date4 = tuple[int, int, int, int]
type Date5 = tuple[int, int, int, int, int]
type Date6 = tuple[int, int, int, int, int, int]
type Date7 = tuple[int, int, int, int, int, int, int]
type DateParts = Date3 | Date4 | Date5 | Date6 | Date7


class Strptime(Protocol):
    def __call__(self, date_string: str, format: str, /) -> datetime: ...


class FromTimestamp(Protocol):
    def __call__(self, timestamp: float, *, tz: tzinfo = ...) -> datetime: ...


class DateTimeDispatcher(Protocol):
    @overload
    def __call__(self, value: str, in_format: str) -> Strptime: ...
    @overload
    def __call__(self, value: DateParts) -> type[datetime]: ...
    @overload
    def __call__(self, value: float) -> FromTimestamp: ...


@overload
def datetime_dispatcher(value: str, in_format: str) -> Strptime: ...
@overload
def datetime_dispatcher(value: DateParts) -> type[datetime]: ...
@overload
def datetime_dispatcher(value: float) -> FromTimestamp: ...
def datetime_dispatcher(
    value: str | DateParts | float,
    in_format: str | None = None
    ) -> Strptime | FromTimestamp | type[datetime]:
    if isinstance(value, str):
        if not in_format:
            msg = f"You must inform the date format for {value!r}"
            raise ValueError(msg)
        return datetime.strptime

    if isinstance(value, tuple):
        return datetime

    return datetime.fromtimestamp


@overload
def create_date(
    value: str,
    dispatch: DateTimeDispatcher,
    *,
    in_format: str,
) -> datetime: ...
@overload
def create_date(value: DateParts, dispatch: DateTimeDispatcher) -> datetime: ...
@overload
def create_date(value: float, dispatch: DateTimeDispatcher) -> datetime: ...
def create_date(
    value: str | DateParts | float,
    dispatch: DateTimeDispatcher,
    in_format: str | None = None,
) -> datetime:
    if isinstance(value, str):
        if not in_format:
            msg = f"You must inform the date format for {value!r}"
            raise ValueError(msg)
        return dispatch(value, in_format=in_format)(value, in_format)

    if isinstance(value, tuple):
        dt_field_keys = [
            "year",
            "month",
            "day",
            "hour",
            "minute",
            "second",
            "microsecond",
        ]
        dt_kwargs = dict(zip(dt_field_keys, value, strict=False))
        return dispatch(value)(**dt_kwargs, tzinfo=UTC)

    return dispatch(value)(value)


if __name__ == "__main__":
    sep_print()

    date1 = create_date((1, 1, 1, 10, 25, 59), datetime_dispatcher)
    date2 = create_date("2025-08-19", datetime_dispatcher, in_format="%Y-%m-%d")
    date3 = create_date(1755696515, datetime_dispatcher)

    datefmt = "%d/%m/%Y"
    timefmt = "%H:%M:%S"
    cyan_print(f"{date1:{timefmt}}")
    cyan_print(f"{date2:{datefmt}}")
    cyan_print(f"{date3:{datefmt}}")
