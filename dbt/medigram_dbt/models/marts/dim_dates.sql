{{ config(materialized='table') }}

with dates as (
    select distinct
        date_trunc('day', message_date) as date
    from {{ ref('stg_telegram_messages') }}
)

select
    date,
    extract(day from date) as day,
    extract(month from date) as month,
    extract(year from date) as year,
    to_char(date, 'Day') as weekday
from dates
