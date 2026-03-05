import pandas as pd
import json
try:
    with open("data.txt","r",encoding="utf-8") as f:
        data=f.read()
        print(data)

    if "Error" in data:
        print("Error In Your Data")

except Exception as e:
    print(f"Error Of {e}")

try:

    chunk=data.split("\n\n\n")
    #print(chunks)
    chunks=[c for c in chunk if len(c)>6]
    #print(chunk)

    if "Error" in chunks:
        print("Error")

except Exception as e:
    print(f"Error Of {e}")

def parse_chunk(chunk):
    try:
        chunk=chunk.strip()
        sep_chunk=chunk.split("\n")
        username=sep_chunk[0]
        name=sep_chunk[1]

        number_of_post=int(
                        sep_chunk[2].
                        split(" posts")[0].
                        replace(",","")
                        )
        
        number_of_follower=float(
                                    sep_chunk[3].
                                    split(" followers")[0].
                                    replace(",","").
                                    replace("K","").
                                    replace("M","")
                                )
        if "K" in sep_chunk[3]:
            number_of_follower=int(number_of_follower*1000)
        elif "M" in sep_chunk[3]:
            number_of_follower=int(number_of_follower*1000000)
        else:
            number_of_follower=int(number_of_follower)

        number_of_following=int(
                                sep_chunk[4].
                                split(" following")[0].
                                replace(",","").
                                replace("K","").
                                replace("M","")
                                )
        if "K" in sep_chunk[4]:
            number_of_following=int(number_of_following*1000)
        elif "M" in sep_chunk[4]:
            number_of_following=int(number_of_following*1000000)
        else:
            number_of_following =int(number_of_following)
            

        if len(sep_chunk)>=6:
            type_of_page=sep_chunk[5]
            bio="\n".join(sep_chunk[6:])
        else:
            type_of_page="Unknown"
            bio=""

        return {
                "number_of_post":number_of_post,
                "number_of_follower":number_of_follower,
                "number_of_following":number_of_following,
                "type_of_page":type_of_page,
                "bio":bio
                }
    except Exception as e:
        print(f"Error Of {e}")
        return None

parse_data=[parse_chunk(c) for c in chunks]
print(parse_data)

all_chunk=[]
for chunk in chunks:
    parse_chunks=parse_chunk(chunk)
    if parse_chunks:
       all_chunk.append(parse_chunks)
print(all_chunk)


data_1=pd.DataFrame(all_chunk)
print(data_1.head())
# This Will Save instagram.Csv 
save_data=data_1.to_csv("instagram_data.csv",index=False,encoding="utf-8")
print(f"Your Code Successfully Run {save_data}")


with open("Instagram.json","w",encoding="utf-8") as f:
    save_data=json.dump(all_chunk,f,ensure_ascii=False)
    print(f"Code SuccessfulY Run {save_data}")


#Who Has The Minimum Post
for chunks in all_chunk:
    chunks["number_of_post"]=min(c["number_of_post"] for c in all_chunk)
print(f"Minimum POst--->{chunks}")

#Who Has The Maximum Followers
for chunks in all_chunk:
    chunks["number_of_follower"]=max(c["number_of_follower"] for c in all_chunk)
print(f"Maximum follower-->{chunks}")