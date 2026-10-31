# Organization Enrollment: Look Up an Existing D-U-N-S Number First

Research checked: October 31, 2026. Audience: founders and coding agents assisting with enrollment.

## Start here

Before requesting a new D-U-N-S Number, search [Dun & Bradstreet's official lookup](https://www.dnb.com/duns-pages/look-up). Its [lookup guide](https://www.dnb.com/en-us/smb/duns/duns-lookup.html) explains how to search for your company and troubleshoot mismatched information. Use the appropriate country or regional route if prompted.

Apple explicitly says D&B may already have assigned an organization a number. Not personally requesting one does not establish that none exists. An unsuccessful Apple lookup also does not prove that D&B has no record. See [Apple's D-U-N-S guidance](https://developer.apple.com/help/account/membership/D-U-N-S).

## Why this note exists

The repository maintainer reported that Apple's lookup did not provide a number or the expected email. After a support exchange, a direct D&B search located an existing record for the LLC. The maintainer had not personally requested the number; how it was assigned is unknown.

This is a reported experience, not a controlled comparison of lookup services or proof that every LLC automatically receives a number. The practical recommendation is to try D&B directly early, especially when Apple's lookup stalls. No support correspondence, company identifiers, or private business records are reproduced here.

## Suggested lookup workflow

1. Search D&B using the registered legal name and relevant business address or phone information. Compare candidate records carefully; do not choose a similarly named business.
2. If you find the record, verify its legal entity and location details before using the number for Apple enrollment.
3. If information differs, investigate with D&B rather than assuming a new number is needed. D&B notes that address or phone mismatches can prevent a lookup from finding a company.
4. If no record can be confirmed, follow Apple's linked process to request a free number. A new request should follow investigation, not be the first instruction an agent gives.
5. Account for synchronization: Apple currently says to allow up to two business days for new or updated D&B information to reach Apple. Recheck its published timing before planning enrollment.

Finding a number does not by itself establish eligibility or complete Apple's verification.

## Keep three kinds of identity separate

| Item | What to check |
| --- | --- |
| Person signing in | Apple requires an Apple Account with two-factor authentication and the person's legal name. It recommends using an organization email for that account. |
| Organization enrolling | Apple verifies legal entity status and authority to bind the organization. Its legal name becomes the App Store seller name. A work contact email on the organization's domain and a functioning associated website are required. |
| Payment and business records | Verify the actual purchaser, invoice, payment method, and accounting treatment separately; a login address does not answer all of these questions. |

Source for enrollment requirements: [Apple Developer Program enrollment](https://developer.apple.com/programs/enroll/).

An existing personal Apple Account and an individual Developer Program membership are different things. Do not assume that using a personal login necessarily means enrolling as an individual. Equally, do not assume an existing individual membership can be changed simply by entering an LLC name. Confirm the appropriate enrollment or conversion route with Apple for the account's current status.

## Email and phone-number errors

The maintainer also reported difficulty creating another Apple Account while reusing a phone number. Apple says an unavailable email address or phone number during account creation can mean an account already uses it; its [troubleshooting guidance](https://support.apple.com/en-us/120636) explains the next steps.

A [trusted phone number](https://support.apple.com/en-us/122621) is used to receive two-factor verification codes. Do not conflate that role with an account identifier or an organization's contact phone number. The sources reviewed do not establish a universal rule that every business needs a unique phone number across all these roles. Record the exact error and affected field privately, then ask Apple Support rather than diagnosing the cause from a generic failure message.

## LLC liability is a separate question

This guide does not determine whether a particular account or payment arrangement preserves LLC liability protection. Neither organization enrollment, a D-U-N-S Number, nor paying an expense through an LLC is presented here as a guarantee against piercing the corporate veil. Ask qualified counsel about the legal arrangement and an accountant about payment records and expense treatment.

## Agent instructions and evidence limits

Open the official lookup and guidance links before advising someone to request a number. Never claim every LLC already has one, guarantee enrollment, or infer account restrictions not supported by the exact situation. Do not submit company details, create accounts, accept agreements, or make payments merely because you are researching the process.

Only public documentation and the maintainer's stated experience informed this note. No private records were inspected, no company lookup was performed on the maintainer's behalf, and no enrollment or payment was submitted. Keep all sensitive enrollment documents outside this public repository.
