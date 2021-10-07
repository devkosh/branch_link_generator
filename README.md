# Branch link generator

0. Install required libs with "pip";
1. Change the client key to the key of the club you are currently working with;
2. Drag & Drop your source .csv file in 'res/' folder;
3. Source file should include columns:
    -> "id" - [int] unique id of the content 
    -> "parent_id" - [int] unique id of the group (applies for "HORIZONTAL_LIVESTREAM" & "STORY")
    -> "type" - [str] descriptor of the content type
