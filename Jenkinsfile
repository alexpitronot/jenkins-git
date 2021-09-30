pipeline {
    agent any
    stages {
        stage('emailext') {
            steps {
                emailext attachLog: true, body: 'New Push was detected', compressLog: true, subject: 'Attention!', to: 'agorbach@gmail.com'                
            }
        }
        stage('mail') {
            steps {
                mail bcc: '', body: 'Saomething was changed', cc: 'alexpitronot@gmail.com', from: '', replyTo: '', subject: 'Attension!!!!!!!!!!!', to: 'agorbach@gmail.com'
            }
        }
        
        stage('Print') {
            steps {
                echo 'All Good again 2022!'
            }
        }
    }
}


