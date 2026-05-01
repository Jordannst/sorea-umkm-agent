# Instagram Commands

## `/ig_start`

Memulai workflow Instagram dan menampilkan opsi cepat.

## `/ig_plan <brief>`

Membuat rencana konten.

Output:

- objective
- format recommendation
- hook
- caption angle
- CTA

## `/ig_generate <brief>`

Membuat prompt atau asset visual promosi sesuai brand SOREA.

Execution defaults:

- image generation backend: Leonardo REST v2 `gpt-image-2`
- default quality: `HIGH`
- product/feed/drink/promo visuals must use the canonical transparent SOREA logo as image reference
- profile/identity visuals use the background/profile logo reference
- reject/regenerate outputs with invented or mismatched SOREA logos

Output:

- visual prompt
- aspect ratio
- text overlay suggestion
- logo usage
- generated asset path
- QA status

## `/ig_post`

Posting feed dari asset yang sudah ada atau hasil generate.

## `/ig_story`

Posting story.

## Safety

- Posting publik perlu intent eksplisit.
- Jangan klaim sukses tanpa verifikasi.
- Jika API/browser gagal dua kali di step sama, stop dan inspect.
