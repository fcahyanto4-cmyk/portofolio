import { describe, it, expect } from 'vitest';
import { formatDate, formatCurrency } from '../format';

describe('formatDate', () => {
  it('should format date correctly', () => {
    expect(formatDate('2026-07-15')).toContain('2026');
  });
});

describe('formatCurrency', () => {
  it('should format number to IDR currency', () => {
    expect(formatCurrency(50000)).toContain('Rp');
  });
});
