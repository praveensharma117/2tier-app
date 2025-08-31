{{- define "two-tier-app.serviceAccountName" -}}
{{- if .Values.serviceAccount.name }}
{{ .Values.serviceAccount.name }}
{{- else }}
{{ .Release.Name }}
{{- end }}
{{- end }}
