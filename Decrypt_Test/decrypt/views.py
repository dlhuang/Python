from django.shortcuts import render,redirect
# Create your views here.
def decrypt(request):
    """解密文件"""
    if request.method == "GET":
        return render(request, "decrypt.html")
    else:
        # 获取文件
        pic = request.FILES["pic"]
        # 创建一个文件
        save_path = "E:/%s" % pic.name
        with open(save_path, "wb") as f:
            # 获取上传文件的内容并写入打开的文件
            for content in pic.chunks():
                f.write(content)
        # 返回
        return redirect("/decrypt")
        # return JsonResponse({"msg": "OK!"})

