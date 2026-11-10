# Seedance 2.5 API (ByteDance) on OceanToken

Model id: `bytedance/seedance-2.5`. Text to video, image to video (first and last frame), reference to video (images, video, audio), edit and extend a video. Also as `bytedance/seedance-2.5-upscaled` (720p/1080p) and `bytedance/seedance-2.5-upscaled-4k`.

## Price (USD per second of video, read from the public catalog on 2026-11-10)

| Resolution | Text or image input | With a reference video in the input |
|---|---|---|
| 480p | $0.1028 | $0.0615 |
| 720p | $0.2311 | $0.1382 |
| 1080p | $0.5686 | $0.3402 |

The catalog marks this price as the maker's official price (`catalog_price_basis: "official"`). Seedance is billed by tokens; the catalog converts that to a per-second figure at the standard frame size. A 5-second 720p clip from a prompt is about 5 x $0.2311 = **$1.16**. Live prices: https://oceantoken.ai/models/bytedance/seedance-2.5

## Call it

```bash
export OCEANTOKEN_API_KEY=...
MODEL=bytedance/seedance-2.5 python ../python/video.py
```

or with curl: `MODEL=bytedance/seedance-2.5 ../curl/video.sh`.

What it accepts (durations, aspect ratios, reference limits): `MODEL=bytedance/seedance-2.5 ../curl/video-options.sh`.

## Image to video

```json
{
  "model": "bytedance/seedance-2.5",
  "prompt": "The paper boat drifts out of frame, the camera stays still",
  "seconds": "5",
  "resolution": "720p",
  "frame_images": [
    {"type": "image_url", "frame_type": "first_frame", "image_url": {"url": "https://example.com/start.png"}}
  ]
}
```

With a first frame, Seedance 2.5 keeps the frame's shape. A request carries frames or references, not both. Full field list: https://docs.oceantoken.ai/guides/video
