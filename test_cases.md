# Test Cases

| ID | Test | Expected Result |
|---|---|---|
| TC01 | Open `/` | Home page loads |
| TC02 | Enter English text and select Telugu | Telugu translation is displayed when online service works |
| TC03 | Leave input empty | Warning is shown |
| TC04 | Select Hospital | Hospital phrases are displayed |
| TC05 | Click a phrase | Phrase appears in input box |
| TC06 | Click Speak | Browser microphone starts if supported |
| TC07 | Click Speak Translation | Browser reads translated text |
| TC08 | Copy translation | Translation is copied |
| TC09 | Offline mode with `I need help.` | Telugu/Hindi/etc. offline translation is returned |
| TC10 | Offline mode with unknown phrase | User is told the phrase is not in offline vocabulary |
| TC11 | Online translator unavailable + known phrase | Local fallback is used |
| TC12 | Online translator unavailable + unknown phrase | Clear error message is shown |
| TC13 | Source and target are same | Original text is returned |
| TC14 | Mobile browser | Responsive UI is displayed |
