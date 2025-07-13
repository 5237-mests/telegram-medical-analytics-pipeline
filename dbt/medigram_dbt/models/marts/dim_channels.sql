{{ config(materialized='table') }}

select
    sender_id as channel_id,
    min(message_date) as first_seen,
    count(*) as message_count
from {{ ref('stg_telegram_messages') }}
group by sender_id
