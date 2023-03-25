import os
import shutil
from flask import Flask, render_template, request, send_file
from app.services import read_xlsx, read_xls, fuzzy_merge_export


app = Flask(__name__)

cache_path = os.path.abspath(os.path.join("app", "csv"))
if os.path.exists(cache_path):
    shutil.rmtree(cache_path)

os.mkdir(cache_path)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        files = request.files.getlist("files")
        if files[0].filename[-4:] == "xlsx":
            date = files[1].filename.split("-")[1][:3]
            df1 = read_xlsx(files[0])
            df2 = read_xls(files[1])
            fuzzy_merge_export(df1, df2, date)
            return send_file(
                shutil.make_archive(
                    "both_CSVs",
                    "zip",
                    os.path.join(os.path.abspath("app"), "csv")
                ),
                as_attachment=True,
            )
        else:
            date = files[0].filename.split("-")[1][:3]
            df1 = read_xlsx(files[1])
            df2 = read_xls(files[0])
            fuzzy_merge_export(df1, df2, date)
            return send_file(
                shutil.make_archive(
                    "both_CSVs",
                    "zip",
                    os.path.join(os.path.abspath("app"), "csv")
                ),
                as_attachment=True,
            )
    else:
        return render_template("main.html")
