# Available models
available_models = {
    'tsd' : {
        'ell-tsd' : 'https://e10xa42ufttxnpto.us-east-1.aws.endpoints.huggingface.cloud/v1/',
        # 'tsd-ell' : None,
        'eng-tsd' : 'https://qwzj5ugslxbw5sp0.us-east-1.aws.endpoints.huggingface.cloud/v1/',
        # 'tsd-eng' : None,
        'spa-tsd' : 'https://g3gtpfycldxi0pt0.us-east-1.aws.endpoints.huggingface.cloud/v1/',
        # 'tsd-spa' : 'Quantization pending!',
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