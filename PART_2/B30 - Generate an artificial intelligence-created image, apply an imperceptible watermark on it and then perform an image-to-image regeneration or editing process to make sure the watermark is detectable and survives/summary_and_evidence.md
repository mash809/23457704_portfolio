For this activity, I generated an artificial intelligence-created image and applied an imperceptible watermark to it using a watermarking script. An imperceptible watermark is a hidden marker embedded into the image data so that it is not visible during normal viewing. Unlike a normal watermark, it is not shown as visible text or a logo in one part of the image. Instead, it is hidden within the file data and is meant to be detected later by software.

After applying the watermark, I tested whether it could be recovered from the saved watermarked image. The result that came closest to success was when the decoder returned the character “w” from the original watermarked image. This showed that the watermarking process had at least some detectable effect and that hidden data was partly embedded in the image. However, the full intended watermark was not recovered correctly, so the result was only a partial recovery rather than a complete success.

I then performed image-to-image regeneration, which means using the existing image as input so that an artificial intelligence system generates a new but similar version of it rather than simply copying it. After this regeneration step, the watermark could no longer be recovered reliably. In later tests, the decoder returned either corrupted bytes or empty bytes, showing that the hidden watermark did not survive the regeneration process in a dependable way.

The practical application of this activity is in artificial intelligence content authenticity, provenance, and media verification. Hidden watermarking is useful only if it can remain undetected during normal viewing while still being recoverable after the image has been edited, saved, or regenerated. My results showed that this is difficult in practice. Although the original watermarked image showed partial detectability, the regeneration process weakened or destroyed the watermark enough that it could not be recovered reliably afterward.

This activity helped me understand that cybersecurity is not only about protecting systems and networks, but also about protecting the trustworthiness and origin of digital content. Imperceptible watermarking is a promising idea for verifying artificial intelligence-generated media, but it must be robust enough to survive changes to be practically useful.

<img width="1122" height="1402" alt="image" src="https://github.com/user-attachments/assets/0a745687-5bfd-4d4e-887e-81174737592e" />

<img width="1122" height="1402" alt="watermarked" src="https://github.com/user-attachments/assets/c824e816-8657-49ce-907b-ea2dc1b438b5" />
