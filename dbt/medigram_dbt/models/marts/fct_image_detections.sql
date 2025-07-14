{{ config(materialized='table') }}

select
    det.id as detection_id,
    det.image_file,
    det.class_id,
    det.class_name,
    det.confidence,
    det.bbox,
    msg.message_id,
    msg.message_date,
    msg.sender_id
from {{ source('raw', 'image_detections') }} det
left join {{ ref('stg_telegram_messages') }} msg
  on det.image_file = split_part(msg.image_path, '/', -1)
