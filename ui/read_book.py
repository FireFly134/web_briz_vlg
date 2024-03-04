import asyncio

import pandas as pd


async def date_time(date: str, time: str) -> str:
    f_date = date
    if "." in date:
        date_split = date.split(".")
        f_date = f"{date_split[2]}{date_split[1]}-{date_split[0]}"
    if ";" in time:
        time = f'{time.split(";")[0]}:00'
    return f"{f_date} {time}.000 +0300"


async def main() -> None:
    df = pd.read_excel("book.xlsx", sheet_name="Октябрь 2023", skiprows=1)
    df.rename(
        columns={
            "Unnamed: 1": "Адрес: улица",
            "Unnamed: 2": "№ дома",
            "Unnamed: 3": "№ подъезда",
            "Unnamed: 4": "№ кв",
            "дата.1": "дата2",
            "время.1": "время2",
            "Unnamed: 11": "Неисправность и причина заявки",
            "ФИО механика.1": "Исполнитель, ФИО механика",
            "Unnamed: 16": "примечание",
        },
        inplace=True,
    )
    df.dropna(subset=[df.columns[2], df.columns[3]], inplace=True)
    for idx, row in df.iterrows():
        print(
            idx,
            row["Адрес: улица"],
            row["№ дома"],
            int(row["№ подъезда"]),
            await date_time(str(row["дата"]), str(row["время"])),
        )


if __name__ == "__main__":
    asyncio.run(main())
