import branchio
import pandas as pd

'''
0. Install required libs with "pip";
1. Change the client key to the key of the club you are currently working with;
2. Drag & Drop your source .csv file in 'res/' folder;
3. Source file should include columns:
    -> "id" - [int] unique id of the content 
    -> "parent_id" - [int] unique id of the group (applies for "HORIZONTAL_LIVESTREAM" & "STORY")
    -> "type" - [str] descriptor of the content type
'''

# EDIT HERE
client = branchio.Client("INPUT_YOUR_SECRET_KEY")
df = pd.read_csv('res/NAME_OF_YOUR_FILE.csv')
# FINISH EDITING

df = df.dropna(subset=['id'])
df['id'] = df['id'].str.replace(',', '').astype(int)
df['parent_id'] = df['parent_id'].str.replace(',', '')
df['parent_id'] = df['parent_id'].fillna(0)
df['parent_id'] = df['parent_id'].astype(int)

def simple_link_make(_type, _id):
    _res = client.create_deep_link_url(data={"$deeplink_path": _type + "/" + str(_id)},
                                       skip_api_call=True)
    return _res

def hard_link_make(_type, _id, _parent_id):
    _res = client.create_deep_link_url(data={"$deeplink_path": _type + "/" + str(_parent_id) + "/" + str(_id)},
                                       skip_api_call=True)
    return _res

def make_links(data_frame):
    _df_ = pd.DataFrame()
    for i in data_frame.index:
        _id = data_frame.loc[i]['id']
        _parent = data_frame.loc[i]['parent_id']
        _type = data_frame.loc[i]['type']
        if _parent <= 0:
            res = simple_link_make(_type, _id)
            link = client.create_deep_linking_urls([res])
            x = data_frame.loc[i]
            x['link'] = link
            _df_ = _df_.append(x)
        elif _parent > 0:
            res = hard_link_make(_type, _parent, _id)
            link = client.create_deep_linking_urls([res])
            x = df.loc[i]
            x['link'] = link
            _df_ = _df_.append(x)
    return _df_

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    links_df = make_links(df)
    links_df.to_csv('res/NAME_OF_YOUR_OUTPUT_FILE.csv')
