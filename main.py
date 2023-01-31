import os
from farcaster import MerkleApiClient



if __name__ == "__main__":
    fcc = MerkleApiClient(os.environ.get("MNEMONIC"))
    
    # The API client will automatically cycle through access tokens

    # Example request
    print(fcc.get_me())


    # Your code here
    
    # Like this:

    # while True:
    #     # Do something
    #     pass