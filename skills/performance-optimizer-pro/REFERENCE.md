# Performance Pro Reference ⚡⚡

## 🚀 Checklist de Velocidad (Quick Wins)

1. [ ] **Lazy Routes**: ¿Las páginas del frontend usan `Suspense` y `lazy`?
2. [ ] **Image WebP**: ¿Todas las imágenes estáticas están en formato WebP?
3. [ ] **Memoization**: ¿Se usa `useMemo` o `useCallback` en componentes con renders costosos?
4. [ ] **Gzip/Brotli**: ¿La compresión está activa en el servidor?
5. [ ] **FastAPI Background**: ¿Las tareas largas usan `BackgroundTasks`?
6. [ ] **N+1 Queries**: ¿Se usan `joinedload` en SQLAlchemy (si aplica) para evitar múltiples queries?
7. [ ] **Minification**: ¿El bundle de producción está minimizado?
8. [ ] **Tree Shaking**: ¿Se están importando solo los módulos necesarios de las librerías?
9. [ ] **API Payload**: ¿El JSON de respuesta contiene solo lo necesario (no enviar objetos gigantes)?
10. [ ] **Performance Marks**: ¿Se han añadido tiempos de logueo para procesos críticos?

## 🛠️ Comandos de Análisis

- `npm run build -- --report`: Genera un reporte del bundle (si está configurado).
- `py run.py analyze-queries`: (Script futuro) Analiza logs de DB buscando lentitud.

## 💡 Tip: Renderizado

Usa el "React Profiler" para detectar componentes que se re-renderizan innecesariamente por cambios en objetos que no han cambiado realmente.
