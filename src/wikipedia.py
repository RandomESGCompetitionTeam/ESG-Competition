import re
import numpy as np
import pandas as pd


def wiki_cleanup(x:str):
    x = re.sub("\[.*", "", x)
    x = re.sub(".*\:", "", x)
    return x


def wikipedia_awards() -> pd.DataFrame:
    bussiness_awards_url = "https://en.wikipedia.org/wiki/List_of_business_and_industry_awards"
    national_quality_awards_url = "https://en.wikipedia.org/wiki/List_of_national_quality_awards"
    occupational_awards_url = "https://en.wikipedia.org/wiki/List_of_occupational_health_and_safety_awards"

    bussiness_awards = pd.read_html(bussiness_awards_url)
    international_ba, national_awards = bussiness_awards[0], bussiness_awards[1:]
    national_quality_awards = pd.read_html(national_quality_awards_url)[0]
    occupational_by_country_a, UK_occupational_a, US_occupational_a = pd.read_html(occupational_awards_url)

    # Introducing common format:
    # type - str "bussiness", "quality", "occupational" etc.
    # international - True, False
    # country - str
    # award - str

#     columns = ["type", "international", "country", "award"]
    columns = ["international", "country", "award"]

    # international_ba
    international_ba["international"] = True
    international_ba["country"] = np.NaN
    international_ba = international_ba.rename(columns={"Award": "award"})
#     international_ba = international_ba[columns[1:]]
    international_ba = international_ba[columns]

    national_ba = pd.concat(national_awards)
    national_ba["international"] = False
    national_ba = national_ba.rename(columns={"Award": "award", "Country":"country"})
#     national_ba = national_ba[columns[1:]]
    national_ba = national_ba[columns]
    bussiness_awards = pd.concat([international_ba, national_ba])
#     bussiness_awards["type"] = "bussiness"
    # TODO odfiltorwać wszystkie z kategorią country 'United States / Europe'
    # bussiness_awards[bussiness_awards["country"] == 'United States / Europe'].loc[:,"international"] = True

    national_quality_awards["international"] = False
    national_quality_awards = national_quality_awards.rename(columns={"Name": "award", "Country":"country"})
#     national_quality_awards = national_quality_awards[columns[1:]]
    national_quality_awards = national_quality_awards[columns]
#     national_quality_awards["type"] = "quality"

    occupational_by_country_a["international"] = False
    occupational_by_country_a = occupational_by_country_a.rename(columns={"Award": "award", "Country": "country"})
#     occupational_by_country_a = occupational_by_country_a[columns[1:]]
    occupational_by_country_a = occupational_by_country_a[columns[1:]]
#     occupational_by_country_a["type"] = "occupational"


    UK_occupational_a["international"] = False
    UK_occupational_a = UK_occupational_a.rename(columns={"Award": "award"})
    UK_occupational_a["country"] = "United Kingdom"
#     UK_occupational_a = UK_occupational_a[columns[1:]]
    UK_occupational_a = UK_occupational_a[columns]
#     UK_occupational_a["type"] = "occupational"

    US_occupational_a["international"] = False
    US_occupational_a["country"] = "United States"
    US_occupational_a = US_occupational_a.rename(columns={"Award": "award"})
    US_occupational_a = US_occupational_a[columns]
#     UK_occupational_a["type"] = "occupational"

    occupational_awards = pd.concat([occupational_by_country_a, UK_occupational_a, US_occupational_a])

    awards = pd.concat([bussiness_awards, national_quality_awards, occupational_awards])

    return awards


def main():
    awards = unified_award_format()
    awards["award"] = awards["award"].apply(wiki_cleanup)
    awards.to_csv("data/awards.csv", index=False)


# if __name__=="__main__":
#     main()
