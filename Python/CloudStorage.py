import dropbox

class TransferData: 
    def __init__(self, access_token):
        self.access_token = access_token
    def upLoad_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from,'rb')
        dbx.files_upload(f.read(), file_to)
def main():
    access_token = 'sl.BD5WzW21t56_QOQbgLY3a8CCi3rhBmraurcCIKbFTQcoO6Q-xdioN9b3c0eWK430ReA8eMKTzV0uSohM_WD2mVcU_DksTzfDeJ66RzRxlSNDfMcGyrJzptP60jDTE14cqI8nM9aS2bM'
    transferData = TransferData(access_token)

    file_from = input('Please insert file path')
    file_to = input('Please insert the dropbox path')  # The full path to upload the file to, including the file name

    # API v2
    transferData.upLoad_file(file_from, file_to)
    print("file has been moved")
main()