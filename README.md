# PhotoOrganizer
This Organizer create folders by date of picture taking and copy each files to correspond folder.
File types can be handled are ".JPG" & ".MOV" & ".RAF(RAW)"
Ths operation of this code has dependency for the folder tree.
The folder structure that I assumped is below

D:\InBox\0.Grouped
        \1.JPG
        \1.JPG\SourceFolderA
        \1.JPG\SourceFolderB
        \1.JPG\SourceFolderC ...
        \2.RAW
        \2.RAW\SourceFolderD
        \2.RAW\SourceFolderE
        \2.RAW\SourceFolderF ...

When you execute this python script, this program read the modification date of each file.
If there is not a target folder which has shape as date like 2019-01-19 under 0.Group directory,
this code will create target folder and copy files to their own target folder.