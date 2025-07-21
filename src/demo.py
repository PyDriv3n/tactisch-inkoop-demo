import argparse
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


def generate_kpi_report(input_path, output_base):
    # Lees inkoopdata
    df = pd.read_excel(input_path)

    # Voorbeeld KPI-berekeningen
    # Totale besteding per leverancier
    spend_per_supplier = df.groupby('leverancier')['bedrag'].sum().sort_values(ascending=False)

    # Gemiddelde levertijd (indien kolom 'levertijd' aanwezig)
    if 'levertijd' in df.columns:
        avg_lead_time = df.groupby('leverancier')['levertijd'].mean().round(1)
    else:
        avg_lead_time = None

    # Totale besteding en aantal orders
    total_spend = df['bedrag'].sum()
    total_orders = len(df)

    # Schrijf Excel-output
    excel_path = f"{output_base}.xlsx"
    with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
        spend_per_supplier.to_frame('Totaal Besteding').to_excel(writer, sheet_name='Besteding per Leverancier')
        if avg_lead_time is not None:
            avg_lead_time.to_frame('Gem. Levertijd (dgn)').to_excel(writer, sheet_name='Levertijden')
        summary = pd.DataFrame({
            'KPI': ['Totaal Besteding', 'Aantal Orders'],
            'Waarde': [total_spend, total_orders]
        })
        summary.to_excel(writer, sheet_name='Samenvatting', index=False)

    # Maak PDF-rapport
    pdf_path = f"{output_base}.pdf"
    with PdfPages(pdf_path) as pdf:
        # Pagina 1: Samenvatting
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.axis('off')
        tbl = ax.table(
            cellText=summary.values,
            colLabels=summary.columns,
            cellLoc='center',
            loc='center'
        )
        tbl.auto_set_font_size(False)
        tbl.set_fontsize(12)
        pdf.savefig(fig, bbox_inches='tight')
        plt.close(fig)

        # Pagina 2: Besteding per leverancier
        fig, ax = plt.subplots(figsize=(8, 4))
        spend_per_supplier.plot(kind='bar', ax=ax)
        ax.set_title('Totale besteding per leverancier')
        ax.set_ylabel('Bedrag')
        plt.tight_layout()
        pdf.savefig(fig)
        plt.close(fig)

        # Pagina 3: Gemiddelde levertijd (optioneel)
        if avg_lead_time is not None:
            fig, ax = plt.subplots(figsize=(8, 4))
            avg_lead_time.plot(kind='bar', ax=ax)
            ax.set_title('Gemiddelde levertijd per leverancier (dagen)')
            ax.set_ylabel('Dagen')
            plt.tight_layout()
            pdf.savefig(fig)
            plt.close(fig)

    print(f"Excel-rapport opgeslagen: {excel_path}")
    print(f"PDF-rapport opgeslagen: {pdf_path}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Genereer KPI-rapporten voor tactisch inkopen')
    parser.add_argument('--input', '-i', required=True, help='Pad naar de inkoop-export (Excel)')
    parser.add_argument('--output', '-o', required=True, help='Basisnaam voor outputbestanden (zonder extensie)')
    args = parser.parse_args()
    generate_kpi_report(args.input, args.output)
