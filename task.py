# Importing required packages
import veryfi
import pprint


# +
# Choosing a file

invoice_filename = "Input\invoice2.jpg"

# -

def veryfiOCR(filename: str):
    
    # authentication for Veryfi OCR API
    client_id = 'vrfL6cFwUWVntipoMh0sIHSfyJCEe5wUZsXbRIJ'
    client_secret = 'okTwnHBNwPXULflEnWuvKsxD27dVZ9K2MbPF5v7CJENXGLONc6Ge3HUFiPx4nlpc5gTvS20ow5GN7zKRETC2iek65SfiWIE5ydL0SjbihbcA4f83Z9FB7ETZHBtHGikE'
    username = 'stephenhwking499'
    api_key = '1b902ae9a78e39945e26a345036e36ca'
    
    client = veryfi.Client(client_id, client_secret, username, api_key)
    
    # categories = ['Contractors', 'Utilities', 'Travel']
    # response = client.process_document(filename,categories=categories)
    
    response = client.process_document(filename)
    print(type(response))
    return response



if __name__ == "__main__":
    
    # Passing filepath as an argument
    veryfi_response=veryfiOCR(invoice_filename)
     # Printing few data from invoice
    print("=================")
    
    print("Vendor name:"+veryfi_response["vendor"]["name"])
    print("tax:"+str(veryfi_response["tax"]))
    print("subtotal:"+str(veryfi_response["subtotal"]))
    print("total:"+str(veryfi_response["total"]))
    
    print("=================")
    print("All extracted values")
    # Prints entire response dictionary using prettyPrint
    pprint.pprint(veryfi_response)
