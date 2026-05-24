I selected CVE-2026-6973, which affects Ivanti Endpoint Manager Mobile (EPMM). It is an improper input validation vulnerability affecting on-premises EPMM before 12.6.1.1, 12.7.0.1, and 12.8.0.1, and it allows a remotely authenticated administrator to achieve remote code execution. The main official fix is to update to one of the patched versions.

I then compared responses from ChatGPT, Gemini, and Claude on how to fix or mitigate this vulnerability. All three systems were highly consistent on the main remediation: patching is the primary and most important fix. All three also agreed that configuration changes alone are not sufficient, because the root cause is inside the product’s input validation logic and must be corrected by the vendor patch.

ChatGPT gave a clear and practical answer. It correctly identified the patched versions and explained that configuration changes should only be treated as temporary risk reduction. It also recommended additional mitigation such as reducing the number of administrator accounts, enabling stronger authentication, restricting access to the administrative interface, and monitoring for unusual activity. Its answer was well structured and easy to apply in practice.

Gemini produced a similarly accurate response, but with more emphasis on defensive operations. It also identified patching as the absolute fix and recommended useful supporting controls such as restricting the administrative portal, placing it behind a virtual private network or management network, rotating administrator credentials, and terminating active sessions. Gemini also added useful context by linking the vulnerability to credential theft and chained exploitation.

Claude was also consistent with the other two, but provided the most detailed remediation and mitigation guide. It strongly prioritised patching, identified the same fixed versions, and also emphasised credential rotation, multi-factor authentication, access restrictions, and post-exploitation review. Claude’s response stood out because it also included actions such as reviewing audit logs, checking for unusual processes or outbound connections, and treating the system as potentially compromised if exploitation was suspected. It also noted that the vulnerability only affects on-premises EPMM, not related cloud products, which made the answer more precise.

Overall, the three systems were strongly aligned in their main conclusion:

- upgrade Ivanti EPMM immediately
- restrict administrative access
- rotate credentials
- use stronger administrator protections such as multi-factor authentication
- treat configuration changes as supporting mitigation, not a replacement for patching

The comparison showed that generative artificial intelligence systems can be useful for summarising vulnerability remediation, but they should still be checked against trusted evidence such as official advisories and documented remediation guides. In this case, the three responses were broadly consistent, with the main difference being how much operational detail each one provided. Claude was the most detailed, Gemini was strong on defensive controls, and ChatGPT was the clearest step-by-step summary.
