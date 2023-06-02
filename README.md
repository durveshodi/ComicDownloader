# Comic Downloader

The  Comic Downloader is a Python script that allows you to download manga from the Asura Scans website. You can choose the manga you want to download, select specific chapters, and save them as a CBZ (Comic Book ZIP) file.

## Prerequisites

Before running the script, make sure you have the following installed:

- Python 3.x
- requests library (`pip install requests`)
- tqdm library (`pip install tqdm`)
- requests-html library (`pip install requests-html`)
- BeautifulSoup library (`pip install beautifulsoup4`)

## Usage

1. Open the `asurascans.py` file in a text editor or IDE.

2. Run the script by executing the file.

   ```
   python asurascans.py
   ```

3. The script will start by fetching the list of available manga from the Asura Scans website.

4. Choose the manga you want to download by adding its name to the `DownloadingList` variable. You can add multiple manga by separating their names with commas.

   ```python
   DownloadingList = ['Manga 1', 'Manga 2', 'Manga 3']
   ```

5. Run the script again, and it will start downloading the selected manga.

   - The script will create a folder for each manga in the current directory.
   - Inside each manga folder, separate folders will be created for each chapter.
   - The images of each chapter will be saved in their respective chapter folders.
   - Once all the chapters of a manga are downloaded, they will be compressed into a CBZ file.
   - The original folders will be deleted, leaving only the CBZ files.

## Notes

- The script uses the `Comic_List()` function to fetch the list of available manga from the Asura Scans website.
- The `Comic_List()` function returns a list of comic names and their corresponding links.
- The selected manga names and links are stored in the `DownloadingList` variable.
- The `Chapter()` function takes a manga URL and fetches the list of chapters for that manga.
- The `Chapter()` function returns a list of chapter titles and their corresponding links.
- The `Image_URL()` function takes a chapter title and its link and fetches the URLs of the images in that chapter.
- The `save_image()` function saves the images from the provided URLs to the respective chapter folders.
- The `ZIP()` function compresses the chapter folders into CBZ files.
- The `Folder()` function creates a folder with the provided name if it doesn't already exist.
- The `show()` function is used to display information and messages during the execution of the script.
- The script uses a progress bar from the `tqdm` library to show the progress of the downloading process.

Feel free to modify the script as per your requirements and enjoy downloading comic from Asura Scans!
