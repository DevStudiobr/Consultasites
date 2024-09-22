import whois

def analyze_domain(domain):
    try:
        domain_info = whois.whois(domain)
        print("Informações do Domínio:")
        print(f"Nome: {domain_info.domain_name}")
        print(f"Registrado em: {domain_info.creation_date}")
        print(f"Data de Expiração: {domain_info.expiration_date}")
        print(f"Registrador: {domain_info.registrar}")
    except Exception as e:
        print(f"Erro ao obter informações: {e}")

if __name__ == "__main__":
    domain = input("Digite o domínio a ser analisado: ")
    analyze_domain(domain)
