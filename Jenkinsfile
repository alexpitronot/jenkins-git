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
                mail bcc: '', body: 'Your repository was changed', cc: 'alexpitronot@gmail.com', from: '', replyTo: '', subject: 'Attention!!', to: 'agorbach@gmail.com'
            }
        }
        
        stage('Print') {
            steps {
                echo 'Now all good 30-09'
            }
        }
    }
}


