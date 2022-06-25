# pygame_person_selector

# Install & Run
1. Clone repository
2. create venv in pygame_person_selector directory with Python 3.10
3. install requirements.txt in venv
4. Run app.py

# To access SQL Database on Azure
1. [Overall view to set up your environment variables : AZURE_CLIENT_ID, AZURE_TENANT_ID, AZURE_CLIENT_SECRET](https://docs.microsoft.com/en-us/python/api/overview/azure/identity-readme?view=azure-python#environment-variables) <br>
1.a. [Why use AZURE_CLIENT_ID, AZURE_TENANT_ID, AZURE_CLIENT_SECRET](https://stackoverflow.com/questions/62305938/cant-authenticate-to-keyvault-no-credential-in-this-chain-provided-a-token)
2. Register your app with client/application ID and Tenant ID :
- Azure Active Directory
- New Registration
- Give it a name that identifies your application & Register
- Certificates & Secrets
- New Client Secret
- Give it a name & Add
3. For AZURE_CLIENT_SECRET, use the value, not the ID
4. [Assign a Key Vault access policy](https://docs.microsoft.com/en-us/azure/key-vault/general/assign-access-policy?tabs=azure-portal)