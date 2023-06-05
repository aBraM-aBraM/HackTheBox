<?php

$file = $_GET['file'];
$dir = 'press_package/';
$archive = tempnam(sys_get_temp_dir(), 'archive');
$zip = new ZipArchive();
$zip->open($archive, ZipArchive::CREATE);

if (isset($file)) {
        $content = preg_replace('/\.\.\//', '', $file);
        $filecontent = $dir . $content;
        if (file_exists($filecontent)) {
            if ($filecontent !== '.' && $filecontent !== '..') {
                $content = preg_replace('/\.\.\//', '', $filecontent);
                $zip->addFile($filecontent, $content);
            }
        }
} else {
        $files = scandir($dir);
        foreach ($files as $file) {
                if ($file !== '.' && $file !== '..') {
                        $zip->addFile($dir . '/' . $file, $file);
                }
        }       
}

$zip->close();
header('Content-Type: application/zip');
header("Content-Disposition: attachment; filename=press_release.zip");
header('Content-Length: ' . filesize($archive));

readfile($archive);
unlink($archive);

?>
