
[![ZipInfo](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/Lofi/i17.png)]()
# ZipInfo 
ZipInfo is a powerful tool that allows you to quickly extract information based on a given zipcode. With our easy-to-use interface, simply enter the zipcode and get access to a wealth of data in JSON format. Discover details such as country, latitude, longitude, city, state, province, and more. ZipInfo is the go-to tool for developers, marketers, and researchers who need accurate and reliable location information. Start using ZipInfo today and unlock the power of zipcode data!

# Prompt

```
Given the zip code, extract the information in the following JSON format.

{ "query": { "codes": [ "570032" ], "country": "in" }, "results": { "570032": [ { "postal_code": "570032", "country_code": "IN", "latitude": "12.30140000", "longitude": "76.61690000", "city": "Vijayanagar IV Stage", "state": "Karnataka", "city_en": "Vijayanagar IV Stage", "state_en": "Karnataka", "state_code": "KA", "province": "Mysuru", "province_code": "MY" } ] } }

Here's the zipcode:

{zipcode}
```

## Conversation

**ASSISTANT**: Welcome user, this prompt can be used for extracting the Zip Info
**USER**: 571105
**ASSISTANT**: { "query": { "codes": [ "571105" ], "country": "in" }, "results": { "571105": [ { "postal_code": "571105", "country_code": "IN", "latitude": "12.30920000", "longitude": "76.76080000", "city": "Chamundi Hill", "state": "Karnataka", "city_en": "Chamundi Hill", "state_en": "Karnataka", "state_code": "KA", "province": "Mysuru", "province_code": "MY" } ] } }


