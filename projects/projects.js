const projectCards = document.querySelectorAll('section .card');
const detailLinks = {
  'Kalkulatory składki ubezpieczeniowej': '../sections/projects/insurance-calculators.html',
  'Kalkulator flotowy': '../sections/projects/fleet-calculator.html',
  'Modułowa obsługa danych DamageId': '../sections/projects/damage-id.html',
  'Importy danych z Excela': '../sections/projects/excel-imports.html',
  'Raportowanie Word / Excel / PDF': '../sections/projects/reporting.html',
  'Console Import Tools': '../sections/projects/console-tools.html',
  'REST API + OAuth2': '../sections/projects/rest-oauth.html',
  'Kafka + Avro': '../sections/projects/kafka-avro.html',
  'SignalR — centralne powiadomienia': '../sections/projects/signalr.html',
  'API za Load Balancerem': '../sections/projects/load-balancer.html',
  'Email Dispatcher .NET 8': '../sections/projects/email-dispatcher.html',
  'RabbitMQ + wysyłka maili': '../sections/projects/rabbitmq-email.html',
  'OpenText Captiva': '../sections/projects/opentext-captiva.html',
  'Captiva Farm': '../sections/projects/captiva-farm.html',
  'PowerShell Automation': '../sections/projects/powershell-automation.html',
  'SQL Reporting': '../sections/projects/sql-reporting.html',
  'Apigee Proxies': '../sections/projects/apigee-proxies.html',
  'WCF / WPF / aplikacje konsolowe': '../sections/projects/wcf-wpf.html',
  'Modular Monolith / Microservices': '../sections/projects/modular-monolith.html',
  'Client / API / Services / Domain': '../sections/projects/layered-architecture.html',
  'Skalowanie aplikacji Blazor': '../sections/projects/blazor-scaling.html'
};

projectCards.forEach((card) => {
  const title = card.querySelector('h3')?.textContent.trim();
  const target = detailLinks[title];
  if (!target) return;

  const link = document.createElement('a');
  link.className = 'detail-link';
  link.href = target;
  link.textContent = 'Szczegóły →';
  link.addEventListener('click', (event) => event.stopPropagation());
  card.appendChild(link);
});
