```basic
┌──(kali㉿kali)-[~]
└─$ dirsearch -x 400 -r -u 10.10.78.249

  _|. _ _  _  _  _ _|_    v0.4.1
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 30 | Wordlist size: 10877

Output File: /home/kali/.dirsearch/reports/10.10.78.249/_21-07-19_16-30-15.txt

Error Log: /home/kali/.dirsearch/logs/errors-21-07-19_16-30-15.log

Target: http://10.10.78.249/

[16:30:16] Starting: 
[16:30:17] 301 -  308B  - /js  ->  http://10.10.78.249/js/
[16:30:20] 403 -  290B  - /.ht_wsr.txt
[16:30:20] 403 -  293B  - /.htaccess.bak1
[16:30:20] 403 -  293B  - /.htaccess.orig
[16:30:20] 403 -  295B  - /.htaccess.sample
[16:30:20] 403 -  293B  - /.htaccess.save
[16:30:20] 403 -  294B  - /.htaccess_extra
[16:30:20] 403 -  293B  - /.htaccess_orig
[16:30:20] 403 -  291B  - /.htaccess_sc
[16:30:20] 403 -  291B  - /.htaccessOLD
[16:30:20] 403 -  292B  - /.htaccessOLD2
[16:30:20] 403 -  291B  - /.htaccessBAK
[16:30:20] 403 -  284B  - /.html
[16:30:20] 403 -  283B  - /.htm
[16:30:20] 403 -  289B  - /.htpasswds
[16:30:20] 403 -  293B  - /.htpasswd_test
[16:30:20] 403 -  290B  - /.httr-oauth
[16:30:25] 200 -   14KB - /404.html
[16:30:43] 301 -  316B  - /categories  ->  http://10.10.78.249/categories/
[16:30:46] 301 -  309B  - /css  ->  http://10.10.78.249/css/
[16:30:50] 301 -  311B  - /fonts  ->  http://10.10.78.249/fonts/
[16:30:52] 200 -  942B  - /images/     (Added to queue)
[16:30:52] 301 -  312B  - /images  ->  http://10.10.78.249/images/
[16:30:53] 200 -   16KB - /index.html
[16:30:53] 200 -    2KB - /index.xml
[16:30:54] 200 -  931B  - /js/     (Added to queue)
[16:31:02] 301 -  310B  - /page  ->  http://10.10.78.249/page/
[16:31:06] 301 -  311B  - /posts  ->  http://10.10.78.249/posts/
[16:31:10] 403 -  292B  - /server-status
[16:31:10] 403 -  293B  - /server-status/     (Added to queue)
[16:31:13] 200 -  661B  - /sitemap.xml
[16:31:15] 301 -  310B  - /tags  ->  http://10.10.78.249/tags/
[16:35:49] Starting: images/
[16:35:54] 403 -  297B  - /images/.ht_wsr.txt
[16:35:54] 403 -  300B  - /images/.htaccess.bak1
[16:35:54] 403 -  300B  - /images/.htaccess.orig
[16:35:54] 403 -  300B  - /images/.htaccess.save
[16:35:54] 403 -  301B  - /images/.htaccess_extra
[16:35:54] 403 -  298B  - /images/.htaccess_sc
[16:35:54] 403 -  300B  - /images/.htaccess_orig
[16:35:54] 403 -  299B  - /images/.htaccessOLD2
[16:35:54] 403 -  298B  - /images/.htaccessOLD
[16:35:54] 403 -  298B  - /images/.htaccessBAK
[16:35:54] 403 -  302B  - /images/.htaccess.sample
[16:35:54] 403 -  291B  - /images/.html
[16:35:54] 403 -  296B  - /images/.htpasswds
[16:35:54] 403 -  297B  - /images/.httr-oauth
[16:35:54] 403 -  300B  - /images/.htpasswd_test
[16:35:54] 403 -  290B  - /images/.htm
[16:36:58] Starting: js/
[16:37:06] 403 -  293B  - /js/.ht_wsr.txt
[16:37:06] 403 -  296B  - /js/.htaccess.bak1
[16:37:06] 403 -  296B  - /js/.htaccess.orig
[16:37:06] 403 -  298B  - /js/.htaccess.sample
[16:37:06] 403 -  296B  - /js/.htaccess.save
[16:37:06] 403 -  297B  - /js/.htaccess_extra
[16:37:06] 403 -  296B  - /js/.htaccess_orig
[16:37:06] 403 -  295B  - /js/.htaccessOLD2
[16:37:06] 403 -  294B  - /js/.htaccessOLD
[16:37:06] 403 -  294B  - /js/.htaccess_sc
[16:37:06] 403 -  294B  - /js/.htaccessBAK
[16:37:06] 403 -  286B  - /js/.htm
[16:37:06] 403 -  287B  - /js/.html
[16:37:06] 403 -  296B  - /js/.htpasswd_test
[16:37:06] 403 -  292B  - /js/.htpasswds
[16:37:06] 403 -  293B  - /js/.httr-oauth
[16:38:09] Starting: server-status/
[16:38:16] 404 -  285B  - /server-status/%2e%2e//google.com
[16:38:42] 403 -  367B  - /server-status/a4j/s/3_3_3.Finalorg/richfaces/renderkit/html/css/basic_classes.xcss/DATB/     (Added to queue)
[16:38:42] 403 -  357B  - /server-status/a4j/g/3_3_1.GAorg.richfaces.renderkit.html.Paint2DResource/DATA/     (Added to queue)
[16:38:45] 403 -  372B  - /server-status/admin/fckeditor/editor/filemanager/browser/default/connectors/asp/connector.asp
[16:38:45] 403 -  374B  - /server-status/admin/fckeditor/editor/filemanager/browser/default/connectors/aspx/connector.aspx
[16:38:45] 403 -  356B  - /server-status/admin/fckeditor/editor/filemanager/connectors/asp/connector.asp
[16:38:45] 403 -  353B  - /server-status/admin/fckeditor/editor/filemanager/connectors/asp/upload.asp
[16:38:45] 403 -  372B  - /server-status/admin/fckeditor/editor/filemanager/browser/default/connectors/php/connector.php
[16:38:55] 403 -  380B  - /server-status/all/modules/ogdi_field/plugins/dataTables/extras/TableTools/media/swf/ZeroClipboard.swf
[16:39:12] 403 -  366B  - /server-status/fckeditor/editor/filemanager/browser/default/connectors/asp/connector.asp
[16:39:12] 403 -  368B  - /server-status/fckeditor/editor/filemanager/browser/default/connectors/aspx/connector.aspx
[16:39:12] 403 -  366B  - /server-status/fckeditor/editor/filemanager/browser/default/connectors/php/connector.php
[16:39:16] 403 -  375B  - /server-status/includes/fckeditor/editor/filemanager/browser/default/connectors/php/connector.php
[16:39:15] 403 -  359B  - /server-status/includes/fckeditor/editor/filemanager/connectors/php/connector.php
[16:39:16] 403 -  377B  - /server-status/includes/fckeditor/editor/filemanager/browser/default/connectors/aspx/connector.aspx
[16:39:16] 403 -  375B  - /server-status/includes/fckeditor/editor/filemanager/browser/default/connectors/asp/connector.asp
[16:39:16] 403 -  359B  - /server-status/includes/fckeditor/editor/filemanager/connectors/asp/connector.asp
[16:39:16] 403 -  356B  - /server-status/includes/fckeditor/editor/filemanager/connectors/asp/upload.asp
[16:39:17] 403 -  376B  - /server-status/jolokia/exec/com.sun.management:type=DiagnosticCommand/jfrStart/filename=!/tmp!/foo
[16:39:17] 403 -  376B  - /server-status/jolokia/exec/com.sun.management:type=DiagnosticCommand/jvmtiAgentLoad/!/etc!/passwd
[16:39:17] 403 -  366B  - /server-status/jolokia/exec/com.sun.management:type=DiagnosticCommand/vmSystemProperties
[16:39:17] 403 -  361B  - /server-status/jolokia/exec/com.sun.management:type=DiagnosticCommand/vmLog/disable
[16:39:17] 403 -  373B  - /server-status/jolokia/exec/com.sun.management:type=DiagnosticCommand/vmLog/output=!/tmp!/pwned
[16:39:17] 403 -  383B  - /server-status/jolokia/exec/com.sun.management:type=DiagnosticCommand/compilerDirectivesAdd/!/etc!/passwd
[16:39:18] 403 -  357B  - /server-status/learn/ruubikcms/ruubikcms/tiny_mce/plugins/filelink/filelink.php
[16:39:18] 403 -  361B  - /server-status/learn/ruubikcms/ruubikcms/website/scripts/jquery.lightbox-0.5.js.php
[16:39:18] 403 -  368B  - /server-status/learn/ruubikcms/ruubikcms/tiny_mce/plugins/tinybrowser/tb_standalone.js.php
[16:39:18] 403 -  365B  - /server-status/learn/ruubikcms/ruubikcms/tiny_mce/plugins/tinybrowser/tb_tinymce.js.php
[16:39:32] 403 -  370B  - /server-status/script/jqueryplugins/dataTables/extras/TableTools/media/swf/ZeroClipboard.swf
[16:39:32] 403 -  351B  - /server-status/scripts/ckeditor/ckfinder/core/connector/asp/connector.asp
[16:39:33] 403 -  380B  - /server-status/servlet/oracle.xml.xsql.XSQLServlet/soapdocs/webapps/soap/WEB-INF/config/soapConfig.xml
[16:39:33] 403 -  380B  - /server-status/servlet/Oracle.xml.xsql.XSQLServlet/soapdocs/webapps/soap/WEB-INF/config/soapConfig.xml
[16:39:33] 403 -  367B  - /server-status/servlet/com.ibm.as400ad.webfacing.runtime.httpcontroller.ControllerServlet
[16:39:39] 403 -  356B  - /server-status/typo3conf/ext/static_info_tables/ext_tables_static+adt-orig.sql
[16:39:48] Starting: server-status/a4j/s/3_3_3.Finalorg/richfaces/renderkit/html/css/basic_classes.xcss/DATB/
[16:40:24] 403 -  446B  - /server-status/a4j/s/3_3_3.Finalorg/richfaces/renderkit/html/css/basic_classes.xcss/DATB/admin/fckeditor/editor/filemanager/browser/default/connectors/asp/connector.asp
[16:40:34] 403 -  454B  - /server-status/a4j/s/3_3_3.Finalorg/richfaces/renderkit/html/css/basic_classes.xcss/DATB/all/modules/ogdi_field/plugins/dataTables/extras/TableTools/media/swf/ZeroClipboard.swf
[16:41:00] 403 -  449B  - /server-status/a4j/s/3_3_3.Finalorg/richfaces/renderkit/html/css/basic_classes.xcss/DATB/includes/fckeditor/editor/filemanager/browser/default/connectors/asp/connector.asp
[16:41:00] 403 -  451B  - /server-status/a4j/s/3_3_3.Finalorg/richfaces/renderkit/html/css/basic_classes.xcss/DATB/includes/fckeditor/editor/filemanager/browser/default/connectors/aspx/connector.aspx
[16:41:04] 403 -  450B  - /server-status/a4j/s/3_3_3.Finalorg/richfaces/renderkit/html/css/basic_classes.xcss/DATB/jolokia/exec/com.sun.management:type=DiagnosticCommand/jvmtiAgentLoad/!/etc!/passwd
[16:41:04] 403 -  447B  - /server-status/a4j/s/3_3_3.Finalorg/richfaces/renderkit/html/css/basic_classes.xcss/DATB/jolokia/exec/com.sun.management:type=DiagnosticCommand/vmLog/output=!/tmp!/pwned
[16:41:04] 403 -  457B  - /server-status/a4j/s/3_3_3.Finalorg/richfaces/renderkit/html/css/basic_classes.xcss/DATB/jolokia/exec/com.sun.management:type=DiagnosticCommand/compilerDirectivesAdd/!/etc!/passwd
[16:41:04] 403 -  450B  - /server-status/a4j/s/3_3_3.Finalorg/richfaces/renderkit/html/css/basic_classes.xcss/DATB/jolokia/exec/com.sun.management:type=DiagnosticCommand/jfrStart/filename=!/tmp!/foo
[16:41:23] 403 -  444B  - /server-status/a4j/s/3_3_3.Finalorg/richfaces/renderkit/html/css/basic_classes.xcss/DATB/script/jqueryplugins/dataTables/extras/TableTools/media/swf/ZeroClipboard.swf
[16:41:24] 403 -  454B  - /server-status/a4j/s/3_3_3.Finalorg/richfaces/renderkit/html/css/basic_classes.xcss/DATB/servlet/Oracle.xml.xsql.XSQLServlet/soapdocs/webapps/soap/WEB-INF/config/soapConfig.xml
[16:41:24] 403 -  454B  - /server-status/a4j/s/3_3_3.Finalorg/richfaces/renderkit/html/css/basic_classes.xcss/DATB/servlet/oracle.xml.xsql.XSQLServlet/soapdocs/webapps/soap/WEB-INF/config/soapConfig.xml
[16:41:37] Starting: server-status/a4j/g/3_3_1.GAorg.richfaces.renderkit.html.Paint2DResource/DATA/
[16:42:10] 403 -  436B  - /server-status/a4j/g/3_3_1.GAorg.richfaces.renderkit.html.Paint2DResource/DATA/admin/fckeditor/editor/filemanager/browser/default/connectors/asp/connector.asp
[16:42:10] 403 -  436B  - /server-status/a4j/g/3_3_1.GAorg.richfaces.renderkit.html.Paint2DResource/DATA/admin/fckeditor/editor/filemanager/browser/default/connectors/php/connector.php
[16:42:10] 403 -  438B  - /server-status/a4j/g/3_3_1.GAorg.richfaces.renderkit.html.Paint2DResource/DATA/admin/fckeditor/editor/filemanager/browser/default/connectors/aspx/connector.aspx
[16:42:22] 403 -  444B  - /server-status/a4j/g/3_3_1.GAorg.richfaces.renderkit.html.Paint2DResource/DATA/all/modules/ogdi_field/plugins/dataTables/extras/TableTools/media/swf/ZeroClipboard.swf
[16:42:41] 403 -  441B  - /server-status/a4j/g/3_3_1.GAorg.richfaces.renderkit.html.Paint2DResource/DATA/includes/fckeditor/editor/filemanager/browser/default/connectors/aspx/connector.aspx
[16:42:41] 403 -  439B  - /server-status/a4j/g/3_3_1.GAorg.richfaces.renderkit.html.Paint2DResource/DATA/includes/fckeditor/editor/filemanager/browser/default/connectors/asp/connector.asp
[16:42:42] 403 -  439B  - /server-status/a4j/g/3_3_1.GAorg.richfaces.renderkit.html.Paint2DResource/DATA/includes/fckeditor/editor/filemanager/browser/default/connectors/php/connector.php
[16:42:45] 403 -  437B  - /server-status/a4j/g/3_3_1.GAorg.richfaces.renderkit.html.Paint2DResource/DATA/jolokia/exec/com.sun.management:type=DiagnosticCommand/vmLog/output=!/tmp!/pwned
[16:42:45] 403 -  447B  - /server-status/a4j/g/3_3_1.GAorg.richfaces.renderkit.html.Paint2DResource/DATA/jolokia/exec/com.sun.management:type=DiagnosticCommand/compilerDirectivesAdd/!/etc!/passwd
[16:42:45] 403 -  440B  - /server-status/a4j/g/3_3_1.GAorg.richfaces.renderkit.html.Paint2DResource/DATA/jolokia/exec/com.sun.management:type=DiagnosticCommand/jvmtiAgentLoad/!/etc!/passwd
[16:42:45] 403 -  440B  - /server-status/a4j/g/3_3_1.GAorg.richfaces.renderkit.html.Paint2DResource/DATA/jolokia/exec/com.sun.management:type=DiagnosticCommand/jfrStart/filename=!/tmp!/foo
[16:43:01] 403 -  434B  - /server-status/a4j/g/3_3_1.GAorg.richfaces.renderkit.html.Paint2DResource/DATA/script/jqueryplugins/dataTables/extras/TableTools/media/swf/ZeroClipboard.swf
[16:43:02] 403 -  444B  - /server-status/a4j/g/3_3_1.GAorg.richfaces.renderkit.html.Paint2DResource/DATA/servlet/Oracle.xml.xsql.XSQLServlet/soapdocs/webapps/soap/WEB-INF/config/soapConfig.xml
[16:43:02] 403 -  444B  - /server-status/a4j/g/3_3_1.GAorg.richfaces.renderkit.html.Paint2DResource/DATA/servlet/oracle.xml.xsql.XSQLServlet/soapdocs/webapps/soap/WEB-INF/config/soapConfig.xml

Task Completed
```

```bash
┌──(kali㉿kali)-[~]
└─$ dirsearch -x 400 -r -u 10.10.226.166/images       

  _|. _ _  _  _  _ _|_    v0.4.1
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 30
Wordlist size: 10877

Output File: /home/kali/.dirsearch/reports/10.10.226.166/images_21-07-25_11-44-25.txt

Error Log: /home/kali/.dirsearch/logs/errors-21-07-25_11-44-25.log

Target: http://10.10.226.166/images/

[11:44:26] Starting: 
[11:44:30] 403 -  298B  - /images/.ht_wsr.txt
[11:44:30] 403 -  301B  - /images/.htaccess.orig
[11:44:30] 403 -  301B  - /images/.htaccess.bak1
[11:44:30] 403 -  303B  - /images/.htaccess.sample
[11:44:30] 403 -  300B  - /images/.htaccessOLD2
[11:44:30] 403 -  301B  - /images/.htaccess_orig
[11:44:30] 403 -  292B  - /images/.html
[11:44:30] 403 -  302B  - /images/.htaccess_extra
[11:44:30] 403 -  301B  - /images/.htaccess.save
[11:44:30] 403 -  298B  - /images/.httr-oauth
[11:44:30] 403 -  299B  - /images/.htaccessBAK
[11:44:30] 403 -  299B  - /images/.htaccess_sc
[11:44:30] 403 -  291B  - /images/.htm
[11:44:30] 403 -  299B  - /images/.htaccessOLD
[11:44:30] 403 -  301B  - /images/.htpasswd_test
[11:44:30] 403 -  297B  - /images/.htpasswds

Task Completed
```