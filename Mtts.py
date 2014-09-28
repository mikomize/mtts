import sublime_plugin
import os
import re


class Mtts(sublime_plugin.WindowCommand):
    def run(self):
        d = os.path.dirname(self.window.project_file_name())

        sourcePath = d
        source = self.window.active_view().settings().get("mtts_source")
        if source is not None:
            sourcePath += "/" + source

        found = []
        for root, dirs, files in os.walk(d):
            for file in files:
                if file.endswith(".sublime-snippet"):
                    found.append(os.path.join(root, file))

        outputPath = d
        output = self.window.active_view().settings().get("mtts_output")
        if output is not None:
            outputPath += "/" + output

        if not os.path.exists(outputPath):
            raise Exception("output path not exists (" + outputPath + ")")

        for file in found:
            f = open(file, "r")
            content = f.read()
            found = re.findall(r"<multiTabTrigger>(.*)</multiTabTrigger>", content)
            if len(found) is 0:
                continue

            multi = found[0].split(",")
            for tab in multi:
                stab = tab.strip()
                newContent = re.sub(r"<tabTrigger>.*</tabTrigger>", "<tabTrigger>" + stab + "</tabTrigger>", content)
                newContent = re.sub(r"<multiTabTrigger>.*</multiTabTrigger>", "", newContent)

                newFileName = outputPath + "/_generated_" + stab + "_" + os.path.basename(file)
                nf = open(newFileName, "w")
                nf.write(newContent)
                print(newFileName)

        print("done.")



