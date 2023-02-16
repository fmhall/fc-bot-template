import os
from farcaster import Warpcast
# from farcaster.models import Parent

# The client will automagically cycle through access tokens
client = Warpcast(os.environ.get("MNEMONIC"), rotation_duration=1)

# Stream new casts, and if one contains "foo", reply "bar"
for cast in client.stream_casts():
    if cast:
        print(cast.author.username, ":")
        print(cast.text)
        print("----")
        # fcc.post_cast("bar", parent=Parent(fid=cast.author.fid, hash=cast.hash))
        pass
