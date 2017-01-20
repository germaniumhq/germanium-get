
from tqdm import tqdm
import urllib
import zipfile


class HeaderAwareUrlOpener(urllib.FancyURLopener):
    def __init__(self, *args, **kw):
        urllib.FancyURLopener.__init__(self, *args, **kw)
        self.addheader("Cookie", "oraclelicense=accept-securebackup-cookie")

urllib._urlopener = HeaderAwareUrlOpener()


def download(url, file_name):
    def my_hook(t):
      """
      Wraps tqdm instance. Don't forget to close() or __exit__()
      the tqdm instance once you're done with it (easiest using `with` syntax).

      Example
      -------

      >>> with tqdm(...) as t:
      ...     reporthook = my_hook(t)
      ...     urllib.urlretrieve(..., reporthook=reporthook)

      """
      last_b = [0]

      def inner(b=1, bsize=1, tsize=None):
        """
        b  : int, optional
            Number of blocks just transferred [default: 1].
        bsize  : int, optional
            Size of each block (in tqdm units) [default: 1].
        tsize  : int, optional
            Total size (in tqdm units). If [default: None] remains unchanged.
        """
        if tsize is not None:
            t.total = tsize
        t.update((b - last_b[0]) * bsize)
        last_b[0] = b
      return inner

    with tqdm(unit='B', unit_scale=True, miniters=1,
              desc=url.split('/')[-1]) as t:  # all optional kwargs
        urllib.urlretrieve(url,
                           filename=file_name,
                           reporthook=my_hook(t),
                           data=None)


def extract_zip(zip_file, target_folder):
    """
    Extract the given zip file into the target folder.
    """
    if not zip_file:
        raise Exception("You need to specify a zip file to extract.")

    if not target_folder:
        raise Exception("You need to specify a target folder where to extract the zip file.")

    zip_ref = zipfile.ZipFile(zip_file, 'r')
    zip_ref.extractall(target_folder)
    zip_ref.close()

