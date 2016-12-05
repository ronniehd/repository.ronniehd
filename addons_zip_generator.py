""" zip generator """

import os
import zipfile
import bs4
import shutil


class Generator:
    """
		Original code from addons_xml_generator.py
    """

    def __init__(self):
        # generate files
        self._generate_addons_file()
        # notify user
        print "Finished creating zip file"

    def _generate_addons_file(self):
        # addon list
        # x = raw_input("Increase version? Y/N? ").lower()
        x = 'n'
        addons = os.listdir(".")
        # final addons text
        # loop thru and add each addons addon.xml file
        for addon in addons:
            # create path
            _path = os.path.join(addon, "addon.xml")
            try:
                # skip any file or .svn folder
                if not os.path.isdir(addon) or addon == ".svn" or addon == ".git" or addon == ".idea":
                    continue
                # split lines for stripping
                data = open(_path, "r").read()
                soup = bs4.BeautifulSoup(data)
                version = soup.select('addon')[0].attrs.get("version")
                # loop thru cleaning each line
                if x == 'y':
                    new_version = version.split('.')
                    new_version[-1] = str(int(new_version[-1]) + 1)
                    version1 = '.'.join(new_version)
                    open(_path, "w").write(data.replace(version, version1, 1))
                    version = version1
                filename_zip = '.\\' + addon + '.\\' + addon + '-' + version
                print addon
                # adding zip
                zf = zipfile.ZipFile(filename_zip + ".zip", "w")
                for dir_name, sub_dirs, files in os.walk(addon):
                    zf.write(dir_name)
                    for filename in files:
                        if '.zip' not in filename:
                            zf.write(os.path.join(dir_name, filename))
                zf.close()
                # erasing files
                for dir_name, sub_dirs, files in os.walk(addon):
                    for filename in files:
                        if '.zip' not in filename and 'addon.xml' not in filename:
                            os.remove(os.path.join(dir_name, filename))
                    # erase dirs
                    for sub_dir in sub_dirs:
                        shutil.rmtree(os.path.join(dir_name, sub_dir))
            except Exception, e:
                # missing or poorly formatted addon.xml
                print "Excluding %s for %s" % (_path, e,)


if (__name__ == "__main__"):
    # start
    Generator()
