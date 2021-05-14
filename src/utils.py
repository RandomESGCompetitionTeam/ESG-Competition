import numpy as np
import eikon as ek
import pandas as pd
from datetime import datetime



def trimm_news(news_batch:list, upper_boundary_date:datetime, lower_boundary_date:datetime) -> list:
    """
    Trimms news
    
    """
    
    if lower_boundary_date:
        for news_idx in reversed(range(len(news_batch))):
            datetime_reponse = news_batch[news_idx]["publication_date"].replace(tzinfo=None)
            if datetime_reponse >= lower_boundary_date:
                news_batch = news_batch[:news_idx]
                print(datetime_reponse)
                print(news_idx)
                break

    if upper_boundary_date:
        for news_idx in range(len(news_batch)):
            datetime_reponse = news_batch[news_idx]["publication_date"].replace(tzinfo=None)
            if datetime_reponse < upper_boundary_date:
                news_batch = news_batch[news_idx:]
                print(datetime_reponse)
                print(news_idx)
                break  
            
    return news_batch



def drop_based_on_occurance(x:pd.DataFrame, variable:str, condition) -> pd.DataFrame:
    """
    Droppin!
    """
    if isinstance(condition, list):
        condition = list(map(lambda z: z.lower(), condition))
        x["temp_col"] = x[variable].apply(lambda z: any([z.lower() in x for x in condition]))
    elif isinstance(condition, str):
        condition = condition.lower()
        x["temp_col"] = x[variable].apply(lambda z: z.lower() in condition)
    
    

    x = x[x["temp_col"]==False].drop(columns="temp_col")
    
    return x


def news_occurance(ticker, regional_awards:list, international_awards:list, date_to:str, date_from:str):
    """
    We stick to refinitiv convention that date_to predeceeds date_from
    """
    
    def award_check(awards, text):
        return sum([award in text for award in awards])
    
    regional_occurance = 0
    international_occurance = 0
    i=0
    n_df = 0
    
    while date_from != date_to:
        old_date_from = date_from
        
        news = ek.get_news_headlines(query=f"R:{ticker}", date_to=date_to, date_from=date_from, count=100)
        if len(news)==0:
            break
        if i%25==0:
            print(date_from)
        news = news.sort_values("versionCreated", ascending=False).reset_index(drop=True)
        news["text"] = news["text"].apply(lambda x:x.lower())
        date_from = str(news.loc[0, "versionCreated"].date())
        if old_date_from == date_from:
            if n_df>=3:
                n_df=0
                print(f"Stuck, breaking for ticker = {ticker}")
                break
            n_df += 1
        
        regional_occurance += sum(news["text"].apply(lambda x: award_check(regional_awards, x)))
        international_occurance += sum(news["text"].apply(lambda x: award_check(international_awards, x)))
        i+=1
        
                
    occurance = {"Ticker":ticker, 
                 "regional_occurance": regional_occurance, 
                 "international_occurance": international_occurance}
    
    return occurance