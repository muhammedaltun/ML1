'''
For scraping remote jobs and data related, from
stackoverflow.com
'''
import requests
import bs4
import pandas as pd


W   = []                           # web address list
T   = []                           # title list
J   = []                           # job type list
R   = []                           # role list
S   = []                           # salary list
C   = []                           # company list
TE  = []                           # technology
SK  = []
NSK = []

def inside(word, par):
    par = par.replace(',',' ').replace('/',' ').replace('(',' ').replace(')',' ').split()
    for w in [word, word + '.']: 
        if w in par: return True
        elif w.upper() in par: return True
        elif w.capitalize() in par: return True
    return False

A=set()    

skills = ['.net', '.net-3.5', '.net-core', '.net-framework-version', '.netcore', '2d', '32-bit', '3d', 'ab-initio', 'abap', 'abstract-syntax-tree', 'access', 'activemq', 'activiti', 'adapter', 'add-on', 'admin', 'adobe', 'adobe-analytics', 'adobe-captivate', 'adobe-illustrator', 'adobecreativesdk', 'aem', 'agile', 'agile-processes', 'agile-project-management', 'airflow', 'ajax', 'akeneo', 'akka', 'algorithmic-trading', 'amazon-cloudformation', 'amazon-cloudwatch', 'amazon-data-pipeline', 'amazon-dynamodb', 'amazon-ec2', 'amazon-ecs', 'amazon-emr', 'amazon-iam', 'amazon-kinesis', 'amazon-redshift', 'amazon-s3', 'amazon-sqs', 'amazon-web-services', 'amp', 'amplitude', 'ampscript', 'analysis', 'analytics', 'android', 'android-firmware', 'android-framework', 'android-jetpack', 'android-sdk-2.1', 'android-sdk-2.3', 'android-studio', 'android-volley', 'androidx', 'angular', 'angular-fullstack', 'angular-material', 'angular-ui-bootstrap', 'angular6', 'angular7', 'angular8', 'angularjs', 'angularjs-directive', 'annotations', 'ansible', 'apache', 'apache-airflow', 'apache-cloudstack', 'apache-flink', 'apache-kafka', 'apache-nifi', 'apache-pig', 'apache-spark', 'apache2', 'apex', 'apex-code', 'api', 'api-design', 'apm', 'apollo', 'app', 'appian', 'appium', 'apple-watch', 'application-security', 'architecture', 'arcore', 'arduino', 'arm', 'artemis', 'articulate-storyline', 'artificial-intelligence', 'aruba', 'asic', 'asp.net', 'asp.net-core', 'asp.net-core-2.0', 'asp.net-core-mvc', 'asp.net-mvc', 'asp.net-mvc-5', 'asp.net-web-api', 'assembly', 'asynchronous', 'audio', 'audit', 'augmented-reality', 'aura-framework', 'authentication', 'autolayout', 'automated-deployment', 'automated-tests', 'automation', 'automationanywhere', 'autosar', 'autoscaling', 'avaya', 'aws', 'aws-api-gateway', 'aws-cloudformation', 'aws-code-deploy', 'aws-ec2', 'aws-iam', 'aws-iot', 'aws-lambda', 'aws-redshift', 'aws-sdk', 'axapta', 'axure', 'azure', 'azure-active-directory', 'azure-cosmosdb', 'azure-data-factory', 'azure-data-lake', 'azure-databricks', 'azure-devops', 'azure-devops-rest-api', 'azure-functions', 'azure-service-fabric', 'azure-sql-database', 'azure-storage-blobs', 'b2b', 'babel', 'babeljs', 'backbone.js', 'backend', 'backup', 'balsamiq', 'bamboo', 'bar-chart', 'bash', 'bayesian', 'bazel', 'bdd', 'beautifulsoup', 'bgp', 'big-o', 'bigdata', 'bioinformatics', 'bitbucket', 'blockchain', 'blueprint', 'blueprism', 'bluetooth', 'bluetooth-lowenergy', 'bonita', 'boomi', 'boost', 'boot', 'bootstrap', 'bootstrap-4', 'bootstrap-modal', 'bpel', 'bpm', 'bpmn', 'bsd', 'build-automation', 'burp', 'business-intelligence', 'butterknife', 'c', 'c#', 'c#-4.0', 'c++', 'c++11', 'c-cda', 'calypso', 'can-bus', 'cassandra', 'cdi', 'centos', 'cfc', 'charles-proxy', 'checkpoint', 'chef', 'chromium', 'circleci', 'circuit', 'cisco', 'cisco-ios', 'citrix', 'clang', 'clearcase', 'client', 'clojure', 'clojurescript', 'clos', 'cloud', 'cloud-security', 'cloudfoundry', 'cloudfront', 'cmake', 'cmocka', 'cms', 'cocoa', 'codeigniter', 'coffeescript', 'cognos', 'coldfusion', 'combine', 'communication', 'compiler', 'compiler-construction', 'compilers', 'components', 'computational-geometry', 'computer-science', 'computer-vision', 'concurrency', 'config', 'configuration', 'configuration-management', 'confluence', 'connectivity', 'containers', 'contao', 'content-management-system', 'continuous-delivery', 'continuous-deployment', 'continuous-integration', 'controls', 
'conv-neural-network', 'cordova', 'core-bluetooth', 'core-location', 'coreml', 'cortana-intelligence', 'cortex-m', 'couchbase-lite', 'couchdb', 'cqrs', 'crm', 'cryengine', 'cryptography', 'crystal-reports', 'csrf', 'css', 'css3', 'csv', 'cuba', 'cucumber', 'cuda', 'customer', 'cypress', 'd', 'd3.js', 'dagger', 'dagger-2', 'dart', 'dashboard', 'data', 'data-analysis', 'data-ingestion', 'data-lake', 'data-migration', 'data-modeling', 'data-modelling', 'data-science', 'data-structures', 'data-visualization', 'data-warehouse', 'database', 'database-administration', 'database-design', 'database-migration', 'databricks', 'dataflow', 'debian', 'debian-based', 'debugging', 'deep-learning', 'delphi', 'dependency-injection', 'deployment', 'design', 'design-patterns', 'desktop-application', 'detox', 'devops', 'dhcp', 'dicom', 'digital', 'digital-twin', 'directoryservices', 'directx', 'distributed', 'distributed-computing', 'distributed-database', 'distributed-system', 'distribution', 'dita', 'django', 'django-rest-framework', 'dns', 'docker', 'docker-compose', 'docker-swarm', 'doctrine', 'doctrine-orm', 'documentation', 'dojo', 'dom', 'domain-driven-design', 'domain-model', 'drivers', 'dropwizard', 'drupal', 'drupal-7', 'drupal-8', 'dynamics-365', 'dynamics-crm', 'dynamics-crm-2011', 'dynamics-crm-365', 'e-commerce', 'eclipse', 'ecm', 'ecmascript-6', 'edi', 'ef-code-first', 'ejb', 'elastic-beanstalk', 'elastic-beats', 'elastic-stack', 'elasticsearch', 'electron', 'elixir', 'elk', 'elm', 'embedded', 'embedded-linux', 'ember-cli', 'ember-data', 'ember.js', 'emc', 'enterprise-architect', 'entitlements', 'entity-framework', 'enzyme', 'episerver', 'er', 'erlang', 'erp', 'erwin', 'es2015', 'es6', 'esb', 'espresso', 'ethercat', 'ethereum', 'ethernet', 'etl', 'event-driven', 'event-sourcing', 'events', 'excel', 'exchange-server', 'exoplayer', 'express', 'extjs', 'f#', 'fastlane', 'feathersjs', 'ffmpeg', 'fhir', 'fido-u2f', 'figma-api', 'filesystems', 'finance', 'financial', 'firebase', 'firebase-mlkit', 'firewall', 'firmware', 'flask', 'flask-sqlalchemy', 'flexbox', 'fluid-dynamics', 'flutter', 'flux', 'flyway', 'force.com', 'foreman', 'fortran', 'fpga', 'frameworks', 'freertos', 'front-end', 'frontend', 'ftp', 'functional', 'functional-programming', 'functional-testing', 'gallio', 'game-engine', 'gateway', 'gatsby', 'gcc', 'gcp', 'gdal', 'gdb', 'gemfire', 'generics', 'geospatial', 'gherkin', 'gis', 'git', 'git-svn', 'github', 'gitlab', 'gitlab-ci', 'glassfish', 'glide-golang', 'go', 'golang', 'google-analytics', 'google-app-engine', 'google-apps', 'google-bigquery', 'google-cloud', 'google-cloud-dataflow', 'google-cloud-platform', 'google-compute-engine', 'google-data-studio', 'google-kubernetes-engine', 'google-oauth2', 'googlecloud', 'gpu', 'gradle', 'grafana', 'grails', 'grape', 'graph-databases', 'graphene-python', 'graphhopper', 'graphic-design', 'graphics', 'graphql', 'grasshopper', 'graylog', 'grinder', 'groovy', 'grpc', 'gruntjs', 'gsm', 'gsp', 'gstreamer', 'gui', 'gulp', 'gwt', 'h.265', 'hacking', 'hadoop', 'hana', 'hardware', 'hashicorp-vault', 'hashmap', 'haskell', 'havok', 'hbase', 'hdfs', 'heroku', 'hibernate', 'high-availability', 'high-speed-computing', 'hive', 'hl7', 'hl7-fhir', 'hlsl', 'hololens', 'hosting', 'html', 'html5', 'html5-canvas', 'http', 'http4s', 'https', 'hubspot', 'hybrid-cloud', 'hybrid-mobile-app', 'hybris', 'hybris-data-hub', 'iam', 'ibm-doors', 'ibm-mq', 'icinga2', 'ida', 'identity-management',
'ignite', 'iks', 'image', 'image-processing', 'implementation', 'informatica', 'informatica-powercenter', 'infrastructure', 'innodb', 'integration', 'integration-testing', 'intellij-idea', 'interaction-design', 'interface', 'interface-builder', 'intrusion-detection', 'invision-power-board', 'ionic', 'ionic-framework', 'ionic3', 'ios', 'ios6', 'ios7', 'iot', 'ip', 'iphone', 'iso', 'istio', 'itil', 'ivr', 'j2ee', 'jasmine', 'java', 'java-8', 'java-ee', 'java-script', 'java11', 'javascript', 'jax-ws', 'jboss', 'jdbc', 'jdeveloper', 'jenkins', 'jest', 'jestjs', 'jetty', 'jira', 'jira-agile', 'jira-rest-api', 'jira-zephyr', 'jitterbit', 'jmeter', 'jpa', 'jpa-2.0', 'jquery', 'jquery-ui', 'jruby', 'js', 'jsf', 'json', 'json-api', 'jsp', 'jsx', 'juniper', 'junit', 'jupyter-lab', 'jupyter-notebook', 'jvisualvm', 'jvm', 'kafka', 'kanban', 'karma', 'kendo-ui', 'keras', 'kerberos', 'kernel', 'key-value-store', 'kibana', 'kinesis', 'kotlin', 'kotlinx.coroutines', 'kubernetes', 'kvm', 'lambda', 'lamp', 'lan', 'laravel', 'laravel-5', 'lead', 'leader', 'leakcanary', 'less', 'libraries', 'lifecycle', 'lightning', 'linq', 'linux', 'linux-kernel', 'liquid', 'llvm', 'load-balancing', 'loadrunner', 'locust', 'logistics', 'logstash', 'lombok', 'looker', 'low-latency', 'lstm', 'lte', 'lucene', 'lumen', 'lxc', 'mac', 'machine-learning', 'macos', 'magento', 'magento2', 'maintenance', 'makefile', 'manual-testing', 'mapbox-gl-js', 'mapkit', 'mapreduce', 'mapstruct', 'mariadb', 'mariadb-10.1', 'markdown', 'math', 'mathematical-optimization', 'matlab', 'matplotlib', 'maven', 'mcs', 'mdm', 'measurement', 'media', 'medical', 'memcached', 'metadata', 'meteor', 'mfc', 'microcontroller', 'microservices', 'microsoft-dynamics', 'microsoft-dynamics-nav', 'microsoft-teams', 'microsoft-test-manager', 'middleware', 'migration', 'mixpanel', 'mobile', 'mobile-development', 'mobx', 'mocking', 'modbus', 'model-view-controller', 'modeling', 'mongo', 'mongodb', 'mongoose', 'monitoring', 'mqtt', 'ms-office', 'ms-sql', 'mulesoft', 'multicore', 'multiplatform', 'multithreading', 'multivariate-testing', 'mvc', 'mvp', 'mvvm', 'mysql', 'nagios', 'native', 'nativescript', 'neo4j', 'neoload', 'nessus', 'nestjs', 'netapp', 'netbeans', 'netlify', 'netscaler', 'network', 'network-programming', 'networking', 'neural-network', 'newrelic', 'next.js', 'nexus', 'nginx', 'ngrx', 'nhibernate', 'nlp', 'nms', 'node', 'node.js', 'nodejs', 'nosql', 'npm', 'numeric', 'numpy', 'nutch', 'nuxt.js', 'oauth', 'oauth-2.0', 'object-oriented-design', 'objective-c', 'octopus-deploy', 'odata', 'office-js', 'office365', 'okhttp', 'olap', 'ollydbg', 'ontology', 'ooad', 'oop', 'open-source', 'openapi', 'opencl', 
'opencv', 'opengl', 'opengl-es', 'openid-connect', 'openshift', 'openstack', 'opentext', 'operating-system', 'operations-research', 'optaplanner', 'optimization', 'or-tools', 'oracle', 'oracle-apex', 'oracle-data-integrator', 'oracle-fusion-middleware', 'oracle-rac', 'oracle12c', 'oracledb', 'orleans', 'orm', 'oss', 'osx', 'outlook', 'outlook-addin', 'owasp', 'p2p', 'p5.js', 'paas', 'packer', 'pact', 'pandas', 'parallel-processing', 'patch', 'payment', 'payment-gateway', 'pcf', 'pci', 'pdal', 'pega', 'penetration-testing', 'peoplesoft', 'percona', 'perforce', 'performance', 'performance-testing', 'perl', 'phoenix', 'photoshop', 'php', 'php-7', 'phpunit', 'physx', 'pimcore', 'pipeline', 'pivotal-cloud-foundry', 'platform', 'playframework', 'playstation', 'plotly', 'plsql', 'point-of-sale', 'polarion', 'polymer', 'pos', 'postgres', 'postgresql', 'postman', 'powerbi', 'powershell', 'pp', 'primavera', 'primefaces', 'prismic.io', 'privacy', 'product', 'product-management', 'production-environment', 'progress', 'progress-4gl', 'progressive-web-apps', 'project', 'project-management', 'prometheus', 'protocol-buffers', 'prototype', 'protractor', 'pug', 'pulumi', 'puppet', 'pyqt5', 'pyramid', 'pyspark', 'pytest', 'pyth', 'python', 'python-2.7', 'python-3.x', 'pytorch', 'qa', 'qf-test', 'qlikview', 'qml', 'qt', 'qtestlib', 'qtp', 'r', 'rabbitmq', 'rails', 'rancher', 'ranorex', 'raspberry-pi', 'rational-team-concert', 'razor', 'rdbms', 'react', 'react-hooks', 'react-native', 'react-native-android', 'react-redux', 'react.js', 'reactive-cocoa', 'reactive-programming', 'reactive-swift', 'reactivex', 'reactjs', 'recurrent-neural-network', 'redgate', 'redhat', 'redis', 'redmine', 'redshift', 'redux', 'redux-saga', 'regression', 'relational-database', 'relay', 'release', 'reporting-services', 'responsive', 'responsive-design', 'rest', 'rest-api', 'rest-assured', 'restful', 'restful-architecture', 'retrofit', 'retrofit2', 'reverse-engineering', 'review-board', 'rhel', 'rhino3d', 'roadmap', 'robotics', 'rocksdb', 'rollup', 'routing', 'rpa', 'rspec', 'ruby', 'ruby-on-rails', 'ruby-on-rails-5', 'rule-engine', 'rust', 'rx-android', 'rx-java', 'rx-java2', 'rx-swift', 'rxjs', 's', 'saas', 'sails.js', 'sales', 'salesforce', 'salesforce-communities', 'salesforce-lightning', 'salesforce-service-cloud', 'salt-stack', 'saml', 'sap', 'sap-erp', 'sap-fiori', 'sapui5', 'sas', 'sass', 'sca', 'scala', 'scala-cats', 'scalability', 'scale', 'scalr', 'schema', 'scikit-learn', 'scipy', 'scripting', 'scrum', 'scrumboard', 'scss', 'scss-lint', 'sdk', 'sdlc', 'search', 'security', 'selenium', 'selenium-webdriver', 'selinux', 'semantic-web', 'sensors', 'sentiment-analysis', 'sequel', 'sequencing', 'server', 'serverless', 'serverless-framework', 'service-discovery', 'servicenow', 'servlets', 'sharepoint', 'sharepoint-2013', 'sharepoint-online', 'shell', 'shopify', 'shopware', 'signal-processing', 'signalr', 'silex', 'simulation', 'sinatra', 'single-page-application', 'single-sign-on', 'sip', 'sitecore', 'sitecore-commerce-server', 'sketch', 'skype-for-business', 'slack', 'smartcontracts', 'smtp', 'snowflake', 'soa', 'soap', 'soapui', 'soc', 'software-defined-radio', 'software-design', 'software-distribution', 'software-quality', 'solid', 'solid-principles', 'solidity', 'solidus', 'solr', 'soql', 'spark', 'specflow', 'spinnaker', 'splunk', 'spree', 'spring', 'spring-boot', 'spring-cloud-netflix', 'spring-mvc', 'springboot', 'sprint', 'sql', 
'sql-loader', 'sql-parser', 'sql-server', 'sql-server-2016', 'sqlalchemy', 'sqlite', 'sre', 'ss7', 'ssas', 'ssd', 'ssis', 'ssis-2012', 'ssl', 'ssrs', 'ssrs-2008', 'st', 'stack', 'standards-compliance', 'startup', 'static', 'static-analysis', 'static-code-analysis', 'statistics', 'stl', 'stm32', 'storage', 'storybook', 'stripe-payments', 'styled-components', 'substrate', 'svg', 'svm', 'svn', 'swagger', 'swift', 'swift3', 'swiftui', 'swing', 'switching', 'sybase', 'symfony', 'symfony2', 'symfony3', 'symfony3.x', 'synchronization', 'sysadmin', 'system', 'system-administration', 'system-design', 'systemmanagement', 'tableau', 'tableau-server', 'task-runner-explorer', 'tcp', 'tcp-ip', 'tdd', 'teamcity', 'technical-interviewing', 'telecommunication', 'templates', 'tensorflow', 'teradata', 'terraform', 'test', 'testcafe', 'testing', 'testng', 'testrail', 'text-classification', 'tfs', 'thin-client', 'threadx', 'three.js', 'tibco', 'time-series', 'tin-can-api', 'tomcat', 'toolchain', 'topic-modeling', 'tosca', 'tpm', 'trading', 'travis', 'travis-ci', 'trello', 'tsql', 'twitter-bootstrap', 'type-systems', 'types', 'typescript', 'typo3', 'typoscript', 'ubuntu', 'ucd', 'uft-api', 'uhd', 'ui', 'ui-automation', 'uikit', 'uipath', 'umbraco', 'uml', 'unit-testing', 'unity', 'unity3d', 'unix', 'unreal-engine4', 'usability', 'usaorithm', 'usb', 'user-interaction', 'user-interface', 'ux', 'vaadin', 'vagrant', 'varnish', 'vast', 'vb.net', 'vba', 'vdi', 'veeam', 'verilog', 'verity', 'version-control', 'versioncontrol', 'vhdl', 'video', 'video-recording', 'video-streaming', 'view', 'virtual-machine', 'virtual-reality', 'virtualization', 'virus-scanning', 'visual-studio', 'visual-studio-2010', 'visual-studio-2012', 'visual-studio-2015', 'visual-studio-2017', 'visual-studio-2019', 'visualforce', 'visualisation', 'vlan', 'vmware', 'voip', 'vpn', 'vsto', 'vue-component', 'vue.js', 'vuejs', 'vuejs2', 'vuetify', 'vuex', 'vulkan', 'vxml', 'wan', 'warehouse', 'wcf', 'web', 'web-analytics', 'web-application-design', 'web-application-firewall', 'web-applications', 'web-component', 'web-deployment', 'web-frameworks', 'web-frontend', 'web-service', 'web-services', 'web-technologies', 'webdriver-io', 'webdynpro', 'webgl', 'weblogic', 'webmethods-caf', 'webpack', 'webrtc', 'websocket', 'wechat', 'white-box-testing', 'wicket', 'wildfly', 'windbg', 'window', 'windows', 'winforms', 'wireframe', 'wireshark', 'wordpress', 'wpf', 'writing', 'wso2', 'x86', 'xamarin', 'xamarin.forms', 'xbox-live', 'xcode', 'xctest', 'xen', 'xhtml', 'xilinx', 'xml', 'xslt', 'xunit', 'yii2', 'yocto', 'zabbix', 'zend-framework', 'zendesk', 'zeromq']

print('number of skills to be checked: ',len(skills))


# Gather the remote jobs' addresses into the set A

for k in range(1,23):                                        # limit is range(1,23)
    page = requests.get('https://stackoverflow.com/jobs/remote-developer-jobs?sort=i&pg='+ str(k)) 
    soup = bs4.BeautifulSoup(page.content,"html.parser")

    links = soup.findAll("a", class_="s-link s-link__visited")
    for link in links:
        A.add(link.get("href"))
    print(len(A))
# print(A)


A= list(A)
for a in A:                                                              # for each job link do
    wa = 'https://stackoverflow.com'+a                                   # take web address 
    W.append(wa)
    page = requests.get(wa)
    soup = bs4.BeautifulSoup(page.content,"html.parser")
    fc900 = soup.find("a", class_="fc-black-900")                        # take job title
    T.append(fc900.text)
    fwbold = soup.findAll("span", class_="fw-bold", limit=3)             # take job type and role
    J.append(fwbold[0].text)
    if len(fwbold)==3: R.append(fwbold[2].text)
    else: R.append("NA")
    fc700 = soup.findAll("a", class_="fc-black-700", limit=5)            # take company name
    if fc700==[]: C.append("NA") 
    else: C.append(fc700[0].text)
    salary = soup.findAll("span", class_="-salary pr16", limit=5)        # take salary
    if salary==[]: S.append("NA")
    else: S.append(salary[0].text[0:12])
    posttag = soup.findAll("a", class_="post-tag", limit=10)             # take technologies
    t_string = ""
    counter = 1
    for post in posttag:
        t_string = t_string + post.text + "  "
        counter  = counter + 1
    TE.append(t_string)

    pars = soup.findAll("p")
    string = ''
    for par in pars:
        string = string + par.text +' '
    li = soup.findAll("li")
    for l in li:
        string = string + l.text + ' '
    skills_in_pars = ''
    nskills = 0
    for skill in skills:
        if inside(skill, string):
            skills_in_pars = skills_in_pars + ', ' + skill
            nskills = nskills + 1
    SK.append(skills_in_pars[2:])                                        # take skills
    NSK.append(nskills)           



'''
print(len(C))

print(TE)
'''

dic = {'JOB TITLE': T, 'TYPE': J, 'ROLE': R, 'SKILLS': SK, '# SKILLS': NSK, 'TECHNOLOGIES': TE, 'SALARY': S, 'COMPANY': C,'WEB ADDRESS': W}                            # create a dictionary of lists
df= pd.DataFrame(dic)                                                         # create a dataframe
df.to_excel("stack.xlsx", index = False)

# print(df)

    