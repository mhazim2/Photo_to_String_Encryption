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
            <a class="navbar-brand" href="index.php">Encryption</a>
        </div>
        <div class="navbar-header">
            <a class="navbar-brand" href="index2.php">Decryption</a>
        </div>
    </div>
</div>



<div class="container">
    <div class="page-header">
        <h1 style="color: darkgray; text-align:center">Keamanan Informasi | Image Encryptor</h1>
    </div>

    <div class="row">
        <div class="col-lg-12">
            <form class="well" action="upload_encrypt.php" method="post" enctype="multipart/form-data">
                <div class="form-group">
                    <label for="file">Select a file to upload :</label>
                    <input type="file" name="file" id="file">
                </div>
                <div class="form-group">
                    <label for="password">Password here !</label><br>
                    <input type="password" class="from-control"  id="password" name="password" placeholder="Password" required/>
                </div>
                <p class="help-block">Only jpg,jpeg,png and gif file with </p>
                <p class="help-block">maximum size of 1 MB is allowed. </p>
                <div class="form-group">
                    <button type="submit"  class="btn btn-success" style="width: 300px;" value="Upload">Encrypt Now !</button>
                </div>

            </form>
        </div>
    </div>
</div>



</body>
</html>