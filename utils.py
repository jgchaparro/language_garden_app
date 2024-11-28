# Available models
available_models = {
    'tsd' : {
        'ell-tsd' : 'https://e10xa42ufttxnpto.us-east-1.aws.endpoints.huggingface.cloud/v1/',
        # 'tsd-ell' : None,
        # 'eng-tsd' : 'https://rgoyhhcmfy2sv9od.us-east-1.aws.endpoints.huggingface.cloud/v1/',
        # 'tsd-eng' : None,
        # 'spa-tsd' : 'https://rgoyhhcmfy2sv9od.us-east-1.aws.endpoints.huggingface.cloud/v1/',
        # 'tsd-spa' : 'https://rgoyhhcmfy2sv9od.us-east-1.aws.endpoints.huggingface.cloud/v1/',
    }
}

# Language codes
lang_name_to_code = {
    'Tsakonian': 'tsd', 
    'Fala': 'fax',
    'Spanish' : 'spa',
    'English' : 'eng',
    'Greek' : 'ell',
    }

lang_code_to_name = {v: k for k, v in lang_name_to_code.items()}