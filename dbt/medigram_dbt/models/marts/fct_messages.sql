{{ config(materialized='table') }}

select
    msg.message_id,
    msg.message_date,
    msg.text,
    msg.has_media,
    msg.image_path,
    ch.channel_id,
    d.date
from {{ ref('stg_telegram_messages') }} msg
left join {{ ref('dim_channels') }} ch
  on msg.sender_id = ch.channel_id
left join {{ ref('dim_dates') }} d
  on date_trunc('day', msg.message_date) = d.date
