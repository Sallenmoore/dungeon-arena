import subprocess

# from webassets.filter import Filter, register_filter


def dartsass(path="static/sass/main.scss", output="static/style.css", **kwargs):
    print(f"==========================> dartsass  {path}, {output}, {kwargs}")
    subprocess.run(["sass", f"{path}:{output}"], capture_output=True)


# class SassFilter(Filter):
#     name = "dartsass"

#     def output(self, _in, out, **kwargs):
#         print(f"==========================> dartsass  {_in}, {out}, {kwargs}")
#         subprocess.run(["sass", f"{kwargs.get('output')}:{output_path}"])

#     def input(self, _in, out, **kwargs):
#         out.write(_in.read())


# register_filter(SassFilter)
