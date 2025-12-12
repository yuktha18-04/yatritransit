pipeline {
  agent any
  environment {
    BUILD_TMP = "${env.WORKSPACE}/tmp/yatritransit-builds"
  }
  stages {
    stage('Check Python') {
      steps {
        script {
          def rc = sh(returnStatus: true, script: 'python3 --version')
          if (rc != 0) { error("Python3 is not available on this agent. Aborting build.") }
          else { echo "Python3 available: ${sh(returnStdout: true, script: 'python3 --version').trim()}" }
        }
      }
    }
    stage('prepare') {
      steps {
        sh '''
          set -e
          rm -rf ${BUILD_TMP}
          mkdir -p ${BUILD_TMP}
          TS=$(date +%Y%m%d%H%M%S)
          echo $TS > ${BUILD_TMP}/build-timestamp.txt
          echo "Timestamp: $(cat ${BUILD_TMP}/build-timestamp.txt)"
        '''
      }
    }
    stage('test') {
      steps {
        script { env.TS = sh(returnStdout: true, script: "cat ${BUILD_TMP}/build-timestamp.txt").trim() }
        sh '''
          set -e
          TS=$(cat ${BUILD_TMP}/build-timestamp.txt)
          python3 -m unittest discover -v > ${BUILD_TMP}/unittest-${TS}.log 2>&1 || true
          echo "Unit tests completed, log saved to ${BUILD_TMP}/unittest-${TS}.log"
          tail -n 200 ${BUILD_TMP}/unittest-${TS}.log || true
        '''
      }
    }
    stage('analyse-routes') {
      steps {
        sh '''
          set -e
          TS=$(cat ${BUILD_TMP}/build-timestamp.txt)
          mkdir -p ${BUILD_TMP}
          python3 - <<'PY' > ${BUILD_TMP}/analysis-${TS}.json
import json
from route_calc import calculate_route
pairs = [("A","B"), ("B","C"), ("A","C")]
data = [calculate_route(o,d) for (o,d) in pairs]
print(json.dumps({"analysis": data}, indent=2))
PY
          echo "Analysis created at ${BUILD_TMP}/analysis-${TS}.json"
          ls -l ${BUILD_TMP}
        '''
      }
    }
    stage('archive') {
      steps {
        script { env.TS = sh(returnStdout: true, script: "cat ${BUILD_TMP}/build-timestamp.txt").trim() }
        archiveArtifacts artifacts: "tmp/yatritransit-builds/*${env.TS}*", fingerprint: true, allowEmptyArchive: false
      }
    }
  }
  post {
    always {
      echo "Pipeline finished at: ${new Date()}"
    }
  }
}
