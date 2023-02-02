import os
from farcaster import MerkleApiClient
# from farcaster.models import Parent


if __name__ == "__main__":
    fcc = MerkleApiClient(os.environ.get("MNEMONIC"))
    
    # The API client will automatically cycle through access tokens

    # Example request
    print(fcc.get_me())


    # Your code here
    
    # Like this:

    for cast in fcc.stream_casts(max_counter=120):
        print(cast)
        if cast and "foo" in cast.text:
            # fcc.post_cast("bar", parent=Parent(fid=cast.author.fid, hash=cast.hash))
            pass