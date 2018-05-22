<!DOCTYPE html>
<html lang="en">
<head>
    <title>Keamanan Informasi | image encriptor</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
</head>

<body>
<!-- Static navbar -->
<div class="navbar navbar-default navbar-static-top">
    <div class="container">
        <div class="navbar-header">
            <a class="navbar-brand" href="index.php" style="color: hotpink">Encryption</a>
        </div>
        <div class="navbar-header">
            <a class="navbar-brand" href="index2.php" style="color: hotpink">Decryption</a>
        </div>
    </div>
</div>


<div class="container">
    <div class="page-header">
        <h1 style="color: hotpink; text-align:center">Keamanan Informasi | Image Decryptor</h1>
    </div>
    <div class="row">
        <div class="col-lg-12">
            <form class="well" action="upload_decrypt.php" method="post" enctype="multipart/form-data">
                <div class="form-group">
                    <label for="file">Select a file to upload :</label>
                    <input type="file" name="file"><br>

                    <label for="password">Your Password Please :</label><br>
                    <input type="password" name="password" placeholder="Password" required/>
                    <p class="help-block">Only txt file with maximum size of 1 MB is allowed.</p>
                </div>
                <input type="submit" style="width: 300px;" class="btn btn-primary" value="Upload">
            </form>
        </div>
    </div>
</div>


</body>
</html>