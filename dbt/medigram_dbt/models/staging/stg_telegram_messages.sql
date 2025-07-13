{{ config(materialized='view') }}

with source as (
  select * from {{ source('raw', 'telegram_messages') }}
),

cleaned as (
  select
    id as message_id,
    date::timestamp as message_date,
    text,
    sender_id,
    has_media,
    image_path
  from source
)

select * from cleaned
