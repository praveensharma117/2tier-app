{{- define "two-tier-app.serviceAccountName" -}}
{{- if .Values.serviceAccount.create }}
{{- default (include "two-tier-app.fullname" .) .Values.serviceAccount.name }}
{{- else }}
default
{{- end }}
{{- end }}
