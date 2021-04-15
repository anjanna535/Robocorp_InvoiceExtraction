# Importing required packages
import veryfi
import pprint


# +
# Choosing a file

invoice_filename = "Input\invoice2.jpg"

# -

def veryfiOCR(filename: str):
    
    # authentication for Veryfi OCR API
    #below details can be found in Keys section in Veryfi account
    client_id = 'Client_id'
    client_secret = 'client_secret'
    username = 'username'
    api_key = 'api_key'
    
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
