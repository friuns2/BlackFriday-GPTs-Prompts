
[![X12 EDI to JSON Convertor](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/illustrative/illus_6.png)]()
# X12 EDI to JSON Convertor 
The X12 EDI to JSON Convertor is responsible in parsing the X12 EDI and then build or generate the JSON response to the corresponding EDI based content

# Prompt

```
You are now supposed to act as an expert in performing the X12 EDI Parsing and to JSON. You will be provided with the EDI sample and your job is to parse the X12 EDI format-based content and then generate the JSON based parsed information. Please do not generate your own responses. Just include the parsed EDI JSON.

{{ EDI }}
```

## Conversation

**ASSISTANT**: {

  "ISA": {

    "authorization_info_qualifier": "00",

    "authorization_information": "",

    "security_info_qualifier": "00",

    "security_information": "",

    "interchange_sender_qualifier": "01",

    "interchange_sender_id": "000123456",

    "interchange_receiver_qualifier": "ZZ",

    "interchange_receiver_id": "PARTNERID",

    "date": "090827",

    "time": "0936",

    "repetition_separator": "U",

    "version_number": "00401",

    "control_number": "000000055",

    "acknowledgment_requested": "0",

    "usage_indicator": "T",

    "component_separator": ">"

  },

  "GS": {

    "functional_id_code": "PO",

    "application_sender_code": "000123456",

    "application_receiver_code": "PARTNERID",

    "date": "20090827",

    "time": "1041",

    "group_control_number": "2",

    "responsible_agency_code": "X",

    "version_number": "004010"

  },

  "ST": {

    "transaction_set_identifier_code": "850",

    "header_control_number": "0003"

  },

  "BEG": {

    "purpose_code": "00",

    "purchase_order_type_code": "SA",

    "purchase_order_number": "1000012",

    "date": "20090827"

  },

  "REF": {

    "reference_identification_qualifier": "SR",

    "reference_identification": "N"

  },

  "CSH": {

    "payment_handling_code": "Y"

  },

  "TD5": {

    "transportation_method_code": "",

    "routing": "",

    "shipment_or_vehicle_id_number": "",

    "weight_qualifier": "",

    "weight_unit_code": "",

    "weight": "",

    "volume_unit_qualifier": "",

    "volume": "",

    "lading_quantity": "",

    "packaging_form_code": "",

    "date": "",

    "time": "",

    "reference_identification_qualifier": "",

    "reference_identification": ""

  },

  "N1": {

    "entity_identifier_code": "ST",

    "name": "John Doe"

  },

  "N3": {

    "address_information": "126 Any St"

  },

  "N4": {

    "city_name": "Hauppauge",

    "state_or_province_code": "NY",

    "postal_code": "11788-1234",

    "country_code": "US"

  },

  "PO1": {

    "line_number": "1",

    "quantity_ordered": "1",

    "unit_or_basis_for_measurement_code": "EA",

    "unit_price": "19.95",

    "product_id_qualifier": "VN",

    "product_id": "0054321"

  },

  "CTT": {

    "number_of_line_items": "1",

    "hash_total": "1"

  },

  "SE": {

    "number_of_segments_in_transaction_set": "11",

    "trailer_control_number": "0003"

  },

  "GE": {

    "number_of_transaction_sets_in_functional_group": "1",

    "group_control_number": "2"

  },

  "IEA": {

    "number_of_groups_in_interchange": "1",

    "interchange_control_number": "000000001"

  }

}


